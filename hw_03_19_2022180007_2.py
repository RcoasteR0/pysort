d = [2,5,9,7,3,9,4,6,2,7]

# CMM 출력형식
# (((((A1xA2)xA3)x(A4xA5))x((A6xA7)x(A8xA9)))xA10) 332

#A1xA2
#d[0] * d[1] * d[2]

#A(n)xA(n+1)
#d[n-1] * d[n] * d[n+1]

#A(i~j)xA(j+i~k)
#d[i-1] * d[j] * d[k]

mc = len(d) - 1

INF = float('inf')

C= [[0 for _ in range(mc+1)] for _ in range(mc+1)]
P= [[0 for _ in range(mc+1)] for _ in range(mc+1)]
#p[b][e]=k는 b 부터 e 까지 곱할 때
#최종 곱셈을 k 직후에 한다는 뜻

for sub_problem_size in range(2, mc+1):
    sub_problem_count = mc - sps + 1
    for beg in range(1, spc+1):
        end = beg + sps - 1
        C[beg][end] = INF
        for k in range(beg, end):
            t = ??? + ??? + ???
            #1 = C[beg][k]
            #2 = C[k+1][end]
            #3 = d[?] * d[?] * d[?]
            if C[beg][end] < t:
                C[beg][end] = t
                P[beg][end] = k

def path(i, j):
    if i == j:
        return f'A{i}'
    p = P[i][j]
    return f'({path(i,p)}x{path(p+i,j)})'

print(path(1, mc), C[1][mc])