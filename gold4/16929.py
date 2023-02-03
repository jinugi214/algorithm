n, m = map(int, input().split())

game = []

for _ in range(n):
    game.append(list(input()))

# 출발해서 같은 값을 찾아 다니다가 다시 원래자리로 돌아오면 사이클 완성

visited = [[0] * m for _ in range(n)]  # 방문 확인

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

check = 0


def dfs(color, x, y, start_x, start_y, cnt):
    global check
    if check == 1:
        return

    for i, j in zip(dx, dy):
        nx = x + i
        ny = y + j

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if cnt >= 4 and nx == start_x and ny == start_y:
            check = 1
            return

        if game[nx][ny] == color and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(color, nx, ny, start_x, start_y, cnt+1)
            visited[nx][ny] = 0


for x in range(n):
    if check == 1:
        break
    for y in range(m):  # 옆에 값과 같은 값이면 dfs 돌지 않기
        if y > 0 and game[x][y] == game[x][y - 1]:
            continue
        else:
            visited[x][y] = 1
            dfs(game[x][y], x, y, x, y, 1)


if check:
    print('Yes')
else:
    print('No')
