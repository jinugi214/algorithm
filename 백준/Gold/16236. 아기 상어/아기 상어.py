# 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.
import sys
from collections import deque
from heapq import heappop, heappush

input = sys.stdin.readline

def bfs(sx, sy, move):
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append((sx, sy, move))
    visited[sx][sy] = 1
    eat_lst = []
    while q:  # 현재 먹을 수 있는 건 다 먹고 정렬해서 가장 거리 짧은 거 return 하기
        x, y, m = q.popleft()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if data[nx][ny] == 0 or data[nx][ny] == size_shark: # 0이거나 사이즈 같은 곳은 지나갈 수 있다.
                    q.append((nx, ny, m + 1))
                    visited[nx][ny] = 1
                elif 0 < data[nx][ny] < size_shark: # 먹을 수 있는 물고기 후보로 담기
                    heappush(eat_lst, (m + 1, nx, ny))
                    visited[nx][ny] = 1
    if eat_lst:
        return heappop(eat_lst)
    else:
        return False


N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]

# 아기 상어 위치, 물고기 확인
shark = []
fish = []
sx, sy = 0, 0
for i in range(N):
    for j in range(N):
        if data[i][j] == 9:
            sx, sy = i, j
        elif data[i][j] == 0:
            continue
        else:
            fish.append((i, j))

if len(fish) == 0:
    print(0)
else:
    data[sx][sy] = 0  # 아기상어 위치 초기화
    size_shark = 2  # # 처음에 아기 상어의 크기는 2
    eat_fish = 0  # 아기 상어의 사이즈가 커지기 위해 먹은 생선 개수를 계산
    time = 0  # 초 시간
    while True:
        rlt = bfs(sx, sy, 0) # 현재 먹을 수 있는 거 중 가장 짧은 거리
        if not rlt: # 만약 그런 것이 없거나 더 이상 먹을 물고기 없으면
            break
        else:
            move, nx, ny, = rlt
            fish.remove((nx, ny)) # 먹은 물고기 제거
            data[nx][ny] = 0
            eat_fish += 1
            if eat_fish == size_shark: # 아기상어 크기만큼 물고기를 먹으면
                size_shark += 1 # 진화
                eat_fish = 0
            time += move # 물고기 먹으러 이동한 시간만큼 더해주기
            sx, sy = nx, ny # 시작 위치를 물고기 먹은 위치로 바꿔주기

        if not fish:
            break

    print(time)
