import sys
input = sys.stdin.readline

def dfs(s, val):
    global e, ans
    used[s] = 1

    if ans:
        return

    if s == e:
        ans = val
        return

    for i in node[s]:
        n, v = i
        if node[n] and not used[n]:
            dfs(n, val + v)


N, M = map(int, input().split())

node = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, v = map(int, input().split())
    node[a].append((b, v))
    node[b].append((a, v))

for _ in range(M):
    used = [0] * (N + 1)
    s, e = map(int, input().split())
    ans = 0
    dfs(s, 0)
    print(ans)