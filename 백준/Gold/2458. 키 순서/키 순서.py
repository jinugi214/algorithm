def dfs(now, idx):
    for nex in num[idx]:
        if not check[now][nex]:
            check[now][nex] = 1
            check[nex][now] = 1
            dfs(now, nex)


n, m = map(int, input().split())

num = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    num[a].append(b)

check = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    check[i][i] = 1
    dfs(i, i)

cnt = 0
for i in range(1, n+1):
    if sum(check[i]) == n:
        cnt += 1

print(cnt)
