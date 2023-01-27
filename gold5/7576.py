from collections import deque

m, n = map(int, input().split())

tomato = []

for _ in range(n):
    tomato.append(list(map(int, input().split())))

q = deque()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append([i, j])
            # 첫 익은 토마토 큐에 넣어주기

def bfs():
    while q:
        x, y = q.popleft()

        for i, j in zip(dx, dy):
            nx, ny = x + i, y + j
            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:  # 좌표 확인과 익지 않은 토마토인지 확인
                tomato[nx][ny] = tomato[x][y] + 1  # 횟수를 +1 더해준다
                q.append([nx, ny])


bfs()

tmp = 0

for i in tomato:
    for j in i:
        if j == 0:  # 익지못한 토마토가 있으면
            print(-1)
            exit(0)
    tmp = max(tmp, max(i))  # 행별로 최대값 비교

print(tmp - 1)  # 1로 시작했기 때문에 -1
