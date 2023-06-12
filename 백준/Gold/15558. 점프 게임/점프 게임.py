import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

line = []
for _ in range(2):
    line.append(list(map(int, input().rstrip())))

visited = [[False] * n for _ in range(2)]


def check(x, y, idx):
    return idx < y < n and line[x][y] and not visited[x][y]


def bfs(start):
    q = deque([start])

    cur_idx = 0
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for nx, ny in ((x, y + 1), (x, y - 1), (~x, y + k)):
                # ~x =>  0은 1로, 1은 0
                if ny >= n:
                    return 1
                if check(nx, ny, cur_idx):
                    q.append((nx, ny))
                    visited[nx][ny] = True
        cur_idx += 1
    return 0

print(bfs((0, 0)))
