import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    visited[x][y] = 1
    global rlt
    if rlt:
        return

    if x == N-1 and y == N-1:
        rlt = 1
        return

    move = data[x][y]

    if move >= N:
        return

    if 0 <= x+move < N and not visited[x+move][y]:
        dfs(x+move, y)
    if 0 <= y+move < N and not visited[x][y+move]:
        dfs(x, move+y)

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

rlt = 0
visited = [[0] * N for _ in range(N)]
dfs(0, 0)
if rlt == 0:
    print('Hing')
else:
    print('HaruHaru')