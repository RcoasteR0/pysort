edges=[
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

print('Using Maximul Matching')

n_edges = len(edges)

# build adj set from edges
from collections import defaultdict
g = defaultdict(set)
for i in range(len(edges)):
    u, v, w = edges[i]
    g[u].add(v)
    g[v].add(u)

# 구하려는 Set Cover 해 정점들
vc = set()

import random
vertices = list(range(num_vertex))
covered_edge = 0
while covered_edge < n_edges:
    random_index = random.randint(0, len(vertices) - 1)
    u = vertices.pop(random_index) # randomly select from vertices
    if not g[u]: continue # 이 점 주위에 연결된것이 없다면 (모두 지워졌다면) 넘어간다
    v = next(iter(g[u]))  # u 에 연결된 점 하나 뽑아오기 v=list(g[u])[0] 또는 v=list(g[u]).pop() 도 가능.
    vertices.remove(v)  # v 도 vertices 에서 제거

    # print(f'{random_index=} {u=} {v=}')

    vc.add(u)
    vc.add(v)

    # 모든 점 k 에 대해 u~k, v~k 간선을 삭제한다.
    for n in [u, v]:
        for k in list(g[n]):
            if k in g and n in g[k]:
                g[k].remove(n)
                covered_edge += 1

print(len(vc), vc)
