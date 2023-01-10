def dfs(start, now, value, cnt):
    global ans
    if cnt == n:
        if data[now][start]:
            value += data[now][start]
            if ans > value:
                ans = value
        return
    
    if value > ans:
        return
    
    for i in range(n):
        if not visited[i] and data[now][i]:
            visited[i] = 1
            dfs(start, i, value + data[now][i], cnt + 1)
            visited[i] = 0



n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
ans = 1e9
visited = [0] * n
for i in range(n):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0
print(ans)