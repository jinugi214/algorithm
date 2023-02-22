n = int(input())
case = int(input())

graph = [[] for _ in range(n+1)]

visited = [0] * (n + 1)

rlt = []

for _ in range(case):
    x, y = list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)


def dfs(v):
    rlt.append(v)
    visited[v] = 1

    for i in graph[v]:
        if visited[i] == 0 and graph[i]:
            dfs(i)

dfs(1)

print(len(rlt) - 1)