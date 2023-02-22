'''
# dfs 방식
import sys

sys.setrecursionlimit(5000)

dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]


def dfs(x, y):

    for i, j in zip(dx, dy):
        nx = x + i
        ny = y + j

        if nx >= h or nx < 0 or ny >= w or ny < 0:
            continue

        if island[nx][ny] == 1:
            island[nx][ny] = 0
            dfs(nx, ny)
    else:
        return


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    island = []

    for _ in range(h):
        island.append(list(map(int, input().split())))

    cnt = 0

    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)
'''

# bfs 방식
from collections import deque

def bfs(start_x, start_y):

    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, 1, -1, -1, 1]

    q = deque()
    q.append((start_x, start_y))

    while q:
        x, y = q.popleft()

        for i, j in zip(dx, dy):
            nx = x + i
            ny = y + j

            if nx >= h or nx < 0 or ny >= w or ny < 0:
                continue

            if island[nx][ny] == 1:
                island[nx][ny] = 0
                q.append((nx, ny))


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    island = []

    for _ in range(h):
        island.append(list(map(int, input().split())))

    cnt = 0

    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)

