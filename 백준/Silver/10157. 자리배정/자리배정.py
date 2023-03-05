from collections import deque

# C: 가로 R: 세로
C, R = map(int, input().split())
K = int(input())

data = [[0] * (C + 1) for _ in range(R + 1)]
used = [[0] * (C + 1) for _ in range(R + 1)]
move = ((1, 0), (0, 1), (-1, 0), (0, -1))

idx = 0
num = 1

q = deque()
q.append((1, 1))

while q:
    x, y = q.popleft()
    data[x][y] = num
    used[x][y] = 1
    if num == K:
        print(y, x) # 문제예시는 시계방향이지만 나는 반시계방향으로 진행했기 떄문
        break
    if num == C * R:
        print(0)
        break

    num += 1

    dx, dy = move[idx]

    if 1 <= x + dx <= R and 1 <= y + dy <= C and not used[x + dx][y + dy]:
        nx, ny = x + dx, y + dy
    else:
        idx += 1
        if idx == 4:
            idx = 0
        dx, dy = move[idx]
        nx, ny = x + dx, y + dy

    q.append((nx, ny))
