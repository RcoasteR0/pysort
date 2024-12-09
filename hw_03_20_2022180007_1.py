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

start = 7
## Prim

# Build Graph from Input Edge List
g = { s: dict() for s in range(num_vertex) }
for s,e,w in edges:
    g[s][e] = w
    g[e][s] = w

# Prepare Data Structures
from heapdict import heapdict
mst = []
D = heapdict()
D[start] = 0
origins = dict()
origins[start] = start
completed = set()
sum = 0
# Prim Main Loop
while D:
    to_vertex, weight = D.popitem()
    fr_vertex = origins[to_vertex]
    completed.add(to_vertex)
    if fr_vertex != to_vertex:
        mst.append((fr_vertex, to_vertex, weight))
        sum += weight
    for adj, adj_w in g[to_vertex].items():
        if adj in completed: continue       # 내륙이면 무시
        if adj in D and D[adj] <= adj_w: continue # 존재하고 기존게 싸면 무시
        D[adj] = adj_w
        origins[adj] = to_vertex

print(sum, mst)
# 5549 [(8, 9, 230), (9, 18, 154), (9, 22, 191), (18, 16, 214), (16, 17, 308), 
#  (17, 3, 140), (3, 6, 231), (3, 0, 288), (6, 19, 304), (19, 15, 243), 
#  (19, 20, 318), (20, 11, 113), (15, 14, 320), (0, 21, 346), (21, 12, 260),
#  (12, 5, 261), (5, 7, 101), (5, 13, 234), (13, 1, 325), (21, 2, 335),
#  (15, 4, 399), (4, 10, 234)]

## TSP
# Build Graph from MST
mg = { s: set() for s in range(num_vertex) }
for s,e,w in mst:
    mg[s].add(e)
    mg[e].add(s)

# Make Sequence
seq = [ start ]
current = start
while True:
    if current == start and not mg[start]: break
    for k in mg[current]:
        if k not in seq:
            visit = k
            break
    else:
        visit = list(mg[current])[0]
    mg[current].remove(visit)
    seq.append(visit)
    current = visit
print(seq)
# [8, 9, 18, 16, 17, 3, 0, 21, 2, 21, 12, 5, 13, 1, 13, 5, 7, 5, 12, 21, 
#  0, 3, 6, 19, 20, 11, 20, 19, 15, 4, 10, 4, 15, 14, 15, 19, 6, 3, 17, 16, 
#  18, 9, 22, 9, 8]

# Find Shortcut
visited = set()
index = 0
while index < len(seq):
    current = seq[index]
    if current in visited:
        seq.pop(index)
    else:
        visited.add(current)
        index += 1
seq.append(start)
print(seq)
# [8, 9, 18, 16, 17, 3, 0, 21, 2, 12, 5, 13, 1, 7, 6, 19, 20, 11, 15, 4, 10, 14, 22, 8]