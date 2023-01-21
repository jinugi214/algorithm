# dfs를 사용하는 방식 (python은 재귀제한이 걸려있기 때문에 런타임 에러가 발생한다.)
# 그래서 허용범위를 넓혀주자

import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline
def dfs(v):
    visited[v] = 1

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n + 1)

cnt = 0

# 각 노드를 돌기
for i in range(1, n+1):
    if not visited[i]:
        if not graph[i]: # 연결된 그래프가 없다면
            cnt += 1
            visited[i] = True # 방문 처리
        else: # 연결된 그래프가 있으면
            dfs(i) # 탐색
            cnt += 1

print(cnt)

'''
# bfs를 사용하는 방식

from collections import deque
import sys

input = sys.stdin.readline


def bfs(v, edges, visited):
    q = deque([v])
    visited[v] = True

    while q:
        now = q.popleft()

        for e in edges[now]:
            if not visited[e]:
                q.append(e)
                visited[e] = True


n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

result = 0
visited = [False] * (n + 1)

for i in range(1, n + 1):
    if not visited[i]:
        result += 1
        bfs(i, edges, visited)

print(result)
'''
