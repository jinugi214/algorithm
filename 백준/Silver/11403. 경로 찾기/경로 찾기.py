import sys

input = sys.stdin.readline

N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]

def dfs(x):
    for y in range(N):
        if data[x][y] == 1 and not used[y]:
            used[y] = 1
            dfs(y)
rlt = [[0] * N for _ in range(N)]

for i in range(N):
    y_lst = []
    used = [0] * N
    dfs(i)
    print(*used)