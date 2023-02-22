import sys

input = sys.stdin.readline

N, M = map(int, input().split())

d = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

# 우, 좌, 하, 상
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 최대값 
maxValue = 0

# ㅜ 모양을 제외한 최대값 계산
def dfs(i, j, dsum, cnt):
    global maxValue
    # 모양이 완성되면 최대값 계산
    if cnt == 4: # 아무렇게 4번 움직이면 된다.
        maxValue = max(maxValue, dsum)
        return
    
    # 상, 하, 좌, 우 이동
    for n in range(4):
        ni = i + move[n][0] # x좌표
        nj = j + move[n][1] # y좌표
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            # 방문 표시 및 제거
            visited[ni][nj] = True
            dfs(ni, nj, dsum + d[ni][nj], cnt + 1)
            visited[ni][nj] = False

# ㅜ 모양의 최대값 
def exce(i, j):
    global maxValue
    for n in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = d[i][j]
        for k in range(3):
            # move 배열의 요소를 3개씩만 사용할 수 있도록 하기
            # 012, 123, 230, 301
            t = (n + k) % 4
            ni = i + move[t][0]
            nj = j + move[t][1]
            
            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += d[ni][nj] # 이동한 자리 값 더하기
        # 최대값 갱신
        maxValue = max(maxValue, tmp)

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, d[i][j], 1)
        visited[i][j] = False
            
        exce(i, j)

print(maxValue)