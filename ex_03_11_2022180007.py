import math

# 주어진 좌표 리스트
coords = [
    (527, 416), (471, 625), (880, 13), (1163, 145), (1426, 806),
    (14, 429), (742, 531), (1037, 630), (1025, 879), (377, 257),
    (614, 553), (481, 676), (943, 53), (88, 9), (28, 271),
    (952, 279), (1426, 519), (699, 698), (925, 716), (1132, 414),
    (1371, 238), (1389, 689), (1573, 774), (915, 636), (941, 763),
    (1083, 385), (1297, 588), (764, 389), (1536, 186), (1098, 515),
    (1308, 65), (1111, 550), (566, 422), (124, 105), (620, 332),
    (784, 623), (182, 555), (1413, 451), (1092, 660), (30, 217),
    (525, 148), (1311, 887), (1228, 353), (54, 68), (1155, 838),
]


# 두 점 사이의 유클리드 거리의 제곱 계산 함수
def dist_sq(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return dx * dx + dy * dy


# Brute Force 방식으로 가장 가까운 두 점을 찾는 함수
def brute_force_full(array):
    min_dist_sq = float('inf')
    s, e = -1, -1
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            d_sq = dist_sq(array[i], array[j])
            if d_sq < min_dist_sq:
                min_dist_sq = d_sq
                s, e = i, j
    return s, e, math.sqrt(min_dist_sq)


# D&C 방식으로 가장 가까운 두 점을 찾는 함수
def dnc(px, py):
    def closest_pair_rec(px, py):
        n = len(px)
        if n <= 3:
            return brute_force_rec(px)

        mid = n // 2
        mid_point = px[mid][0]

        Qx = px[:mid]
        Rx = px[mid:]

        Qy = []
        Ry = []
        for point in py:
            if point[0] <= mid_point:
                Qy.append(point)
            else:
                Ry.append(point)

        # 재귀적으로 왼쪽과 오른쪽 부분 문제 해결
        s1, e1, d1_sq = closest_pair_rec(Qx, Qy)
        s2, e2, d2_sq = closest_pair_rec(Rx, Ry)

        # 현재까지의 최소 거리과 그에 해당하는 점 쌍
        if d1_sq < d2_sq:
            d_min_sq = d1_sq
            pair = (s1, e1)
        else:
            d_min_sq = d2_sq
            pair = (s2, e2)

        # Strip 생성: 중간선에서 d_min_sq 이내에 있는 점들
        strip = [point for point in py if abs(point[0] - mid_point) ** 2 < d_min_sq]

        # Strip 내에서 가장 가까운 두 점 찾기
        strip_len = len(strip)
        for i in range(strip_len):
            j = i + 1
            while j < strip_len and (strip[j][1] - strip[i][1]) ** 2 < d_min_sq:
                d_sq = dist_sq(strip[i], strip[j])
                if d_sq < d_min_sq:
                    d_min_sq = d_sq
                    pair = (strip[i][2], strip[j][2])  # 원래 인덱스를 저장
                j += 1

        return pair[0], pair[1], d_min_sq

    def brute_force_rec(array):
        min_dist_sq = float('inf')
        s, e = -1, -1
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                d_sq = dist_sq(array[i], array[j])
                if d_sq < min_dist_sq:
                    min_dist_sq = d_sq
                    s, e = array[i][2], array[j][2]  # 원래 인덱스를 저장
        return s, e, min_dist_sq

    return closest_pair_rec(px, py)


# 전체 알고리즘을 실행하는 함수
def closest_pair(array):
    # 각 점에 원래 인덱스를 포함시킴
    array_with_index = [(point[0], point[1], idx) for idx, point in enumerate(array)]

    # x 기준으로 정렬
    array_sorted_x = sorted(array_with_index, key=lambda point: (point[0], point[1]))
    # y 기준으로 정렬
    array_sorted_y = sorted(array_with_index, key=lambda point: (point[1], point[0]))

    s, e, d_sq = dnc(array_sorted_x, array_sorted_y)

    return s, e, math.sqrt(d_sq)


# 가장 가까운 두 점을 D&C 방식으로 찾기
s_dnc, e_dnc, d_dnc = closest_pair(coords)

# 가장 가까운 두 점을 Brute Force 방식으로 찾기
s_brute, e_brute, d_brute = brute_force_full(coords)

# 결과 출력
print("=== Divide and Conquer (DNC) ===")
print(f'[{s_dnc}]{coords[s_dnc]} - [{e_dnc}]{coords[e_dnc]}, d={d_dnc:.6f}')

print("\n=== Brute Force ===")
print(f'[{s_brute}]{coords[s_brute]} - [{e_brute}]{coords[e_brute]}, d={d_brute:.6f}')