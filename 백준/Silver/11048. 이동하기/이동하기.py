N, M = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        visited[i][j] = data[i-1][j-1] + max(visited[i-1][j], visited[i][j-1], visited[i-1][j-1])

print(visited[N][M])