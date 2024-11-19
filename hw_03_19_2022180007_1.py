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

INF = float('inf')
D = [[INF for _ in range(num_vertex)] for _ in range(num_vertex)]
P = [[-1 for _ in range(num_vertex)] for _ in range(num_vertex)]

for i,j,w in edges:
    D[i][j] = w
    D[j][i] = w

for k in range(num_vertex):
    for i in range(num_vertex):
        if i == k: continue
        for j in range(num_vertex):
            if i == j and j == k and k == i: continue
            v = D[i][k] + D[k][j]
            if D[i][j] > v:
                D[i][j] = v
                P[i][j] = k

def path_str(i, j):
    if i == j:  # 출발지와 목적지가 같으면 바로 반환
        return f"{i}"
    if P[i][j] == -1:  # 경로가 없는 경우
        return f"->{j}"
    k = P[i][j]  # j로 가기 직전 노드
    pik = path_str(i, k)  # i에서 k까지의 경로
    pkj = path_str(k, j)  # k에서 j로의 연결
    return f"{pik}{pkj}"  # 전체 경로를 이어붙임

for from_v in range(num_vertex):
    for to_v in range(num_vertex):
        if from_v != to_v and D[from_v][to_v] < INF:
            path = path_str(from_v, to_v)
            print(f'{from_v}{path} ({D[from_v][to_v]})') # 300 lines

'''
0->6->12->13->1 (1349)
0->6->19->2 (894)
0->21->3 (951)
0->22->4 (822)
0->21->16->5 (1195)
0->6 (343)
0->6->19->7 (1347)
0->21->16->8 (1129)
0->21->10->9 (1077)
0->21->10 (852)
0->6->12->13->11 (1266)
0->6->12 (859)
0->6->12->13 (1128)
0->22->24->14 (933)
0->6->15 (698)
0->21->16 (756)
0->21->17 (931)
0->6->18 (835)
0->6->19 (861)
0->21->16->5->20 (1394)
0->21 (494)
0->22 (303)
0->22->24->23 (959)
0->22->24 (585)
1->13->11->7->19->2 (1034)
1->5->17->3 (979)
1->13->11->7->19->2->18->4 (1609)
1->5 (438)
(중간생략)
18->2->19->7->11->20 (934)
18->6->0->21 (1329)
18->6->22 (748)
18->2->23 (545)
18->14->24 (693)
19->7->11->20 (835)
19->6->0->21 (1355)
19->6->22 (774)
19->2->23 (512)
19->14->24 (783)
20->5->16->21 (900)
20->13->12->6->22 (1368)
20->11->7->19->2->23 (1347)
20->13->12->6->24 (1418)
21->0->22 (797)
21->0->22->24->23 (1453)
21->0->22->24 (1079)
22->24->23 (656)
22->24 (282)
23->24 (374)
'''

