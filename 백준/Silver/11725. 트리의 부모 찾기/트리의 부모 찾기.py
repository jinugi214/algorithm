from collections import deque
def bfs(p):

    q = deque([p])

    while q:
        x = q.popleft()

        for i in node[x]:
            if not used[i]:
                q.append(i)
                used[i] = 1
                node_p[i] = x

N = int(input())

node = [[] for _ in range(N+1)]
used = [0] * (N+1)

node_p = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

bfs(1)

for i in range(2, N+1):
    print(node_p[i])