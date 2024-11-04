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
start = 12

# Edge list를 인접 리스트로 변환
g = {s: {} for s in range(num_vertex)}
for s, e, w in edges:
    g[s][e] = w
    g[e][s] = w

from heapdict import heapdict

D = heapdict()  # 최단 경로 비용 저장
distances = {v: float('inf') for v in range(num_vertex)}  # 모든 노드의 거리 무한대로 초기화
distances[start] = 0
origins = {start: start}  # 최단 경로로 오는 이전 정점 저장
completed = set()  # 방문 완료된 정점들


# 거리 업데이트 함수
def update(s, e, w):
    if e in completed:  # 이미 방문 완료된 정점이면 무시
        return
    new_distance = distances[s] + w
    if new_distance < distances[e]:  # 더 짧은 경로 발견 시 갱신
        distances[e] = new_distance
        D[e] = new_distance
        origins[e] = s


# 시작점에 대한 초기 정보 설정
D[start] = 0

# 다익스트라 알고리즘 메인 루프
while D:
    to_vertex, current_distance = D.popitem()  # 가장 짧은 경로 선택
    completed.add(to_vertex)

    # 인접한 간선들에 대해 거리 업데이트 시도
    for adj, adj_w in g[to_vertex].items():
        update(to_vertex, adj, adj_w)

# 최단 경로 출력
def path_to(to):
    if to not in origins:
        return float('inf'), f"Path to {to} not reachable"

    path = []
    while to != start:
        path.append(to)
        to = origins[to]
    path.append(start)
    path.reverse()
    cost = distances[path[-1]]
    return cost, " -> ".join(map(str, path))

print("\nPaths from start vertex to each vertex:")
for to in range(num_vertex):
    cost, path = path_to(to)
    print(f"{path=} {cost=}")
