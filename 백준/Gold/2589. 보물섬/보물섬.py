import sys
from collections import deque

input = sys.stdin.readline

s, k = map(int, input().split())

data = [list(input()) for _ in range(s)]

def bfs(sx, sy, sdis):
    visited = [[0] * k for _ in range(s)]
    rlt = 0
    q = deque([(sx, sy, sdis)])
    visited[sx][sy] = 1
    while q:
        x, y, dis = q.popleft()
        if rlt < dis:
            rlt = dis

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < s and 0 <= ny < k and not visited[nx][ny] and data[nx][ny] == 'L':
                visited[nx][ny] = 1
                q.append((nx, ny, dis + 1))

    return rlt


ans = 0
for i in range(s):
    for j in range(k):
        if data[i][j] == 'L':
            ans = max(ans , bfs(i, j, 0))

print(ans)