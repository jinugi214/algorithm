from collections import deque
import sys

input = sys.stdin.readline

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dx = [-1, 1, 0, 0, 0, 0] # 높이
dy = [0, 0, 0, 0, -1, 1] # 세로
dz = [0, 0, -1, 1, 0, 0] # 가로


def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                if data[nx][ny][nz] == 0:
                    q.append((nx, ny, nz))
                    data[nx][ny][nz] = data[x][y][z] + 1 # 토마토에 익은 일수 추가해주기


# 상자의 크기 가로 M, 세로 N, 쌓아 올려지는 상자의 수 H
M, N, H = map(int, input().split())

# 3차원 배열 입력
data = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

q = deque()  # 익은 토마토 담는 곳

# 1은 익은 토마토, 0 은 익지 않은 토마토, -1은 토마토가 들어있지 않은 칸

# 첫날에 이미 토마토가 모두 익었는 지 확인
bf_done = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if data[i][j][k] == 1:
                q.append((i, j, k)) # 이미 익어진 토마토를 담아준다.
            elif data[i][j][k] == 0:
                bf_done = True

# 첫날 이미 토마토가 다 익었다면
if not bf_done:
    print(0)
    sys.exit()

# bfs로 토마토를 모두 익게 해준다.
bfs()

ans = 0

# 토마토가 모두 익었는지 확인
af_done = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if data[i][j][k] == 0:
                af_done = True

            # 익는 데 제일 오래 걸린 토마토의 일수를 찾자
            ans = max(ans, data[i][j][k])

if af_done:
    print(-1)
else: # 첫날을 제외해야해서 -1
    print(ans - 1)
