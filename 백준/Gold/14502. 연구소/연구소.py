from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
#
# N 세로크기, M 가로크기
data = [list(map(int, input().split())) for _ in range(N)]
# 1인 벽을 세개 세워야한다.
# 행렬의 최대크기 8x8으로 최악의 경우 모든 경우의 수는 64C3 (41664) 2초이내 완전탐색 가능

safe = []
virus = []
# 0인 곳을 모두 찾아 3개를 뽑는 조합을 통해 완전 탐색을 한다.
# 찾으면서 바이러스 위치도 찾아주자
for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            safe.append((i, j))
        elif data[i][j] == 2:
            virus.append((i, j))

# 0(안전영역)에 벽(1) 3개 놓는 경우의 수를 조합으로 추출
case = list(combinations(safe, 3))

# 우선 안전영역 최대값을 0 설정
ans = 0

# 3개의 벽을 놓는 경우마다 바이러스를 진행시켜 본다.
for i in case:
    # 반복할 때마다 초기화를 위해 2차원 배열을 옮겨준다.
    # 리스트 안 내부 리스트의 주소 값도 달라야 하기 떄문에 깊은 복사
    zone = copy.deepcopy(data)
    for j in i:  # 조합으로 뽑은 3개의 벽을 세워주자
        vx, vy = j
        zone[vx][vy] = 1
    q = deque(virus) # 초기 바이러스
    while q: # 바이러스가 모두 전파될 때까지 반복
        x, y = q.popleft()

        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x + dx, y + dy
            # 범위 확인을 하고 벽이 아니고 안전영역이면 바이러스 전파
            if 0 <= nx < N and 0 <= ny < M and not zone[nx][ny]:
                zone[nx][ny] = 2
                q.append((nx, ny))

    # 안전 영역 확인
    safe_zone = 0
    for n in range(N):
        safe_zone += zone[n].count(0)

    # 안전영역 최댓값 확인
    ans = max(safe_zone, ans)


print(ans)