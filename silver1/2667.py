'''
# DFS 방식
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        for i, j in zip(dx, dy):
            nx = x + i
            ny = y + j
            dfs(nx, ny)
        return True
    return False


n = int(input())

graph = []
num = []

for _ in range(n):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = 0
rlt = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            num.append(cnt)
            rlt += 1
            cnt = 0

print(rlt)
num.sort()
for i in num:
    print(i)
'''
# BFS 방식

from collections import deque


def bfs(graph, x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        for i, j in zip(dx, dy):
            nx = x + i
            ny = y + j
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt


n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)
