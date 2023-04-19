# 시작하는 칸과 끝나는 칸도 포함
# 벽을 한 개 까지 부수고 ( 1을 한번 무시)

import sys
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split())

data = [list(map(int, input().rstrip())) for _ in range(N)]

# 0,0 에서 N-1, M-1 도착하기

# x좌표, y좌표, 현재 횟수, 벽 부순거 T/F
def bfs():
    global ans
    visit = set()
    q = deque([(0, 0, 1, 0)])
    visit.add((0, 0, 0))
    while q:
        x, y, cnt, dt = q.popleft()
        if x == N - 1 and y == M - 1:
            ans = min(ans, cnt)
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and (nx, ny, dt) not in visit:
                if data[nx][ny] == 0:
                    q.append((nx, ny, cnt+1, dt))
                    visit.add((nx, ny, dt))
                elif data[nx][ny] == 1 and dt == 0:
                    q.append((nx, ny, cnt+1, 1))
                    visit.add((nx, ny, 1))
ans = 1e9
bfs()
if ans == 1e9:
    print(-1)
else:
    print(ans)
