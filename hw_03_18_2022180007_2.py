edges = [
    (0, 6, 343), (0, 21, 494), (0, 22, 303), (1, 5, 438), (1, 13, 221),
    (1, 20, 465), (2, 14, 411), (2, 18, 66), (2, 19, 33), (2, 23, 479),
    (3, 9, 150), (3, 17, 158), (3, 21, 457), (4, 14, 214), (4, 15, 305),
    (4, 18, 509), (4, 22, 519), (4, 23, 157), (4, 24, 356), (5, 7, 286),
    (5, 12, 481), (5, 13, 230), (5, 16, 439), (5, 17, 383), (5, 20, 199),
    (6, 12, 516), (6, 15, 355), (6, 18, 492), (6, 19, 518), (6, 22, 256),
    (6, 24, 306), (7, 11, 156), (7, 19, 486), (8, 12, 508), (8, 16, 373),
    (8, 17, 203), (9, 10, 225), (9, 16, 413), (9, 17, 295), (10, 16, 213),
    (10, 21, 358), (11, 13, 138), (11, 20, 193), (12, 13, 269), (12, 16, 135),
    (13, 20, 327), (14, 15, 370), (14, 18, 345), (14, 19, 435), (14, 24, 348),
    (15, 23, 373), (16, 21, 262), (17, 21, 437), (22, 24, 282), (23, 24, 374)
]
num_vertex = 25
start = 8

# Edge list를 인접 리스트로 변환
g = {s: {} for s in range(num_vertex)}
for s, e, w in edges:
    g[s][e] = w
    g[e][s] = w

from heapdict import heapdict

mst = []  # 결과 트리 저장
D = heapdict()  # 최단 경로 비용 저장
origins = dict()  # 최단 경로로 오는 이전 정점 저장
completed = set()  # 내륙에 포함된 점들


# MST에 간선을 추가하는 함수
def append(s, e, w):
    if s <= e:
        mst.append((s, e, w))
    else:
        mst.append((e, s, w))
    mst.sort(key=lambda e: e[0] * 1000 + e[1])  # 정렬하여 보기 좋게 출력


# 비용 업데이트 함수
def update(s, e, w):
    if e in completed:  # 이미 내륙에 속하면 무시
        return
    if e in D and D[e] <= w:  # 기존 비용이 더 작으면 무시
        return
    # D 및 origins 갱신
    D[e] = w
    origins[e] = s


# 시작점에 대한 초기 정보 설정
D[start] = 0
origins[start] = start

# 프림 알고리즘 메인 루프
while D:
    to_vertex, weight = D.popitem()  # 가장 짧은 경로 선택
    fr_vertex = origins[to_vertex]
    completed.add(to_vertex)

    if to_vertex != fr_vertex:  # 시작점에서 시작하는 자기 자신 간선 제외
        append(fr_vertex, to_vertex, weight)

    # 인접한 간선들에 대해 비용 업데이트 시도
    for adj, adj_w in g[to_vertex].items():
        update(to_vertex, adj, adj_w)

# 결과 출력
print("Minimum Spanning Tree:")
print(mst)
