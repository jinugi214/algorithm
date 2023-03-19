import sys
from collections import deque

input = sys.stdin.readline


def bfs(start_x, start_y):
    q = deque()
    q.append((start_x, start_y))
    while q:

        x, y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                # 주변에 배추있으면 배추흰지렁이가 이동한다.
                graph[nx][ny] = 0  # 배추흰지렁이가 지나간 곳은 0으로 바꿔주기
                q.append((nx, ny))  # 배추흰지렁이의 이동을 위해 q에 좌표를 담아준다.


T = int(input())  # 테스트 케이스 입력

for _ in range(T):

    M, N, K = map(int, input().split())  # 배추밭 크기와 배추 개수 입력받기

    graph = [[0] * M for _ in range(N)]  # 배추밭 만들기

    for _ in range(K):  # 배추 심기
        x, y = map(int, input().split())
        graph[y][x] = 1

    ans = 0

    for i in range(N):  # 배추 있으면 지렁이 투척
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                ans += 1  # 배추 흰지렁이 += 1

    print(ans)
