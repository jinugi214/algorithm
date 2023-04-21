import sys

input = sys.stdin.readline

def dfs(x, y, z):
    global answer
    val = data[x][y] # 현재 위치 값

    for i in range(x, x + z):
        for j in range(y, y + z):
            # 시작 값과 현재의 값이 다르면
            if data[i][j] != val:
                # 3 * 3 범위 재귀 탐색
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * z // 3, y + l * z // 3, z // 3)
                return

    if val == -1:
        answer[0] += 1
    elif val == 0:
        answer[1] += 1
    else:
        answer[2] += 1

N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]

answer = [0, 0, 0]

dfs(0, 0, N)

for i in range(3):
    print(answer[i])
