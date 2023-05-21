import sys

input = sys.stdin.readline

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

val = 0

if N == 1 and M == 1:
    val = 6
else:
    for i in range(N):
        val += data[i][0]
        val += data[i][M - 1]
        for j in range(1, M):
            val += abs(data[i][j] - data[i][j - 1])

    for i in range(M):
        val += data[0][i]
        val += data[N - 1][i]
        for j in range(1, N):
            val += abs(data[j][i] - data[j - 1][i])
    val += 2 * N * M
print(val)
