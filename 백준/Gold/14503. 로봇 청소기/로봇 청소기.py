N, M = map(int, input().split())

# 처음에 로봇 청소기가 있는 칸의 좌표 r,c
# d가 0인 경우 북쪽, 1인 경우 동쪽, 2인 경우 남쪽, 3인 경우 서쪽
r, c, d = map(int, input().split())

# 0인 경우 청소되지 않은 빈칸, 1인 경우 벽이 있는 것
data = [list(map(int, input().split())) for _ in range(N)]

# 작동을 시작한 후 작동을 멈출 때까지 청소하는 칸의 개수를 출력한다.

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 시작지 청소하고 시작
ans = 1
data[r][c] = 2
while True:
    for _ in range(4):
        d = (d + 3) % 4 # 3, 2, 1, 0 순으로 계산
        dx, dy = move[d]
        nx, ny = r + dx, c + dy
        if 0 <= nx < N and 0 <= ny < M and not data[nx][ny]:
            data[nx][ny] = 2 # 청소한 곳 2로 표시
            r, c = nx, ny # 좌표 갱신
            ans += 1 # 청소횟수 1 추가
            break
    else:
        dx, dy = move[d]
        nx, ny = r - dx, c - dy # 현재 바라보는 방향 기준으로 후진
        if 0 <= nx < N and 0 <= ny < M and not data[nx][ny] or data[nx][ny] == 2:
            r, c = nx, ny
        elif 0 <= nx < N and 0 <= ny < M and data[nx][ny] == 1:
            # 벽이면 작동 중지
            break

print(ans)