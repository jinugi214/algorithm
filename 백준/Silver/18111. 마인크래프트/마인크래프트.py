# 완전탐색

import sys

input = sys.stdin.readline

# N 가로, M 세로, B 인벤토리에 있는 블록개수
N, M, B = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]


# 두종류의 작업
# 1. 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다. (2초)
# 2. 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다. (1초)
def check(ground, height, b):
    sec = 0 # 높이보다 높으면 걸리는 시간
    need_b = 0 # 높이보다 낮으면 채워넣어야하는 블록 수 (시간)
    for i in range(N):
        for j in range(M): # 모든 블록 탐색
            tmp = ground[i][j] - height # 현재 블록에서 높이 차이 구하기
            if tmp > 0: # 블록이 기준 높이보다 높으면
                b += tmp # 블록을 제거하며 인벤토리에 넣어주자
                sec += 2 * tmp # 시간은 2초가 걸린다.
            else: # 블록이 기준보다 낮으면
                need_b += -tmp # 필요한 블록의 수를 차이만큼 계산해주자
    if b < need_b: # 필요한 블록의 수가 현재 가지고 있는 블록보다 많다면
        return 1e9 # 불가능
    return sec + need_b # 가능한 경우 값을 반환

m_sec = 1e9
m_height = 0
for i in range(256, -1, -1): # 답이 여러개이면 가장 높은 것을 출력해야하기 때문에 256부터 시작
    rlt = check(data, i, B)
    if m_sec > rlt: # 최소시간 찾기
        m_sec = rlt
        m_height = i

# ‘땅 고르기’ 작업에 걸리는 최소 시간과 답이 여러개 있다면 가장 높은 땅의 높이를 출력
print(m_sec, m_height)