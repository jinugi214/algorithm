from collections import deque

def bfs():

    while q:
        x, y = q.popleft()

        if x == go_x and y == go_y:
            return chess[x][y]

        for i, j in zip(dx, dy):
            nx, ny = x + i, y + j

            if 0 <= nx < n and 0 <= ny < n and chess[nx][ny] == 0:
                chess[nx][ny] = chess[x][y] + 1
                q.append([nx, ny])


test_case = int(input())

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(test_case):
    n = int(input())

    chess = [[0] * n for _ in range(n)]

    knight_x, knight_y = map(int, input().split())

    go_x, go_y = map(int, input().split())

    q = deque()
    q.append([knight_x, knight_y])
    print(bfs())

