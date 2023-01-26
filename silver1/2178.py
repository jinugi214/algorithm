'''
# DFS 실행시 ValueError 발생

import sys
sys.setrecursionlimit(5000)


def dfs(x, y, cnt):

    if x == n-1 and y == m-1:
        global rlt
        rlt.append(cnt)
        return

    for i, j in zip(dx, dy):
        nx = x + i
        ny = y + j

        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue

        if graph[nx][ny] == 1:
            graph[nx][ny] = 0
            dfs(nx, ny, cnt+1)
            graph[nx][ny] = 1


n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

dx = [1, 0, -1]
dy = [0, 1, 0]

rlt = []

dfs(0, 0, 1)

print(min(rlt))
'''

# BFS

from collections import deque

def bfs(start_x, start_y, cnt):

    q = deque()

    q.append((start_x, start_y, cnt))

    while q:
        x, y, cnt = q.popleft()

        if x == n - 1 and y == m - 1:
            break

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        for i, j in zip(dx, dy):
            nx = x + i
            ny = y + j

            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny, cnt+1))

    return cnt


n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

print(bfs(0, 0, 1))

