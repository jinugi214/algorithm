from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 1
    cnt = 1
    flag = 0
    while q:
        x, y = q.popleft()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if data[nx][ny] == 0:
                    flag = 1
                elif data[nx][ny] == 2:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    cnt += 1
    return cnt if not flag else 0


N, M = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]

two = []
space = []

for i in range(N):
    for j in range(M):
        if data[i][j] == 2:
            two.append((i, j))
        elif data[i][j] == 0:
            space.append((i, j))

comb_lst = list(combinations(space, 2))

rlt = 0

for c in comb_lst:
    val = 0
    visited = [[0] * M for _ in range(N)]
    for x, y in c:
        data[x][y] = 1

    for x, y in two:
        if not visited[x][y]:
            val += bfs(x, y)

    for x, y in c:
        data[x][y] = 0

    rlt = max(rlt, val)

print(rlt)
