M, N = map(int, input().split())

cnt = 0
mv = 0  # 0은 가로 1은 세로

visited = [[0] * N for _ in range(M)]
visited[0][0] = 1

move = ((0, 1), (1, 0), (0, -1), (-1, 0))

idx = 0
x, y = 0, 0
cnt = 0
while True:
    nx, ny = x + move[idx][0], y + move[idx][1]
    if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0:
        visited[nx][ny] = 1
    else:
        idx += 1
        if idx == 4:
            idx = 0
        cnt += 1
        nx, ny = x + move[idx][0], y + move[idx][1]
        if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0:
            visited[nx][ny] = 1
        else:
            cnt -= 1
            break
    x, y = nx, ny

print(cnt)