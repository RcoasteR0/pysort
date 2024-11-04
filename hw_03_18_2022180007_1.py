# 주어진 데이터
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

# Union-Find 자료구조 초기화
parent = list(range(num_vertex))
rank = [0] * num_vertex

# Union-Find의 find 함수 (경로 압축 적용)
def getRoot(v):
    if parent[v] != v:
        parent[v] = getRoot(parent[v])
    return parent[v]

# Union-Find의 union 함수 (랭크에 기반한 합치기)
def connect(u, v):
    root_u = getRoot(u)
    root_v = getRoot(v)
    if root_u != root_v:
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

# 같은 트리에 속하는지 확인하는 함수
def onSameTree(u, v):
    return getRoot(u) == getRoot(v)

# MST에 간선을 추가하는 함수
mst = []
def append(s, e, w):
    if s <= e:
        mst.append((s, e, w))
    else:
        mst.append((e, s, w))
    mst.sort(key=lambda edge: edge[0] * 1000 + edge[1])  # 정렬

# 최소 신장 트리 생성
edges.sort(key=lambda x: x[2])  # 가중치에 따라 정렬

def spanning():
    return len(mst) >= num_vertex - 1

for s, e, w in edges:
    if spanning():
        break
    if onSameTree(s, e):
        continue
    connect(s, e)
    append(s, e, w)

# 결과 출력
print("Minimum Spanning Tree:")
print(mst)
