# 스도쿠
# dfs + 백트래킹
# 0이 있는곳에 1~9 숫자를 하나씩 넣어서
# 가로, 세로, 3*3구간에 들어갈 수 있는 숫자인지
# 확인하며 탐색해보자!
# python으로 실행시 82% 시간초과

import sys

input = sys.stdin.readline

# x의 세로줄에 val이 있는지 확인
def garo_check(x, val):
    for i in range(9):
        if val == data[x][i]:
            return False
    return True


# y 가로줄에 val이 있는지 확인
def sero_check(y, val):
    for i in range(9):
        if val == data[i][y]:
            return False
    return True


# x, y 좌표가 포함되어 있는 3x3 크기의 사각형의 n이 있는지 확인
def nemo_check(x, y, val):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if val == data[nx + i][ny + j]:
                return False
    return True


# dfs + 백트래킹
def dfs(cnt):
    global flag
    # 빈칸이 모두 채워진다면
    if cnt == len(zero):
        for i in range(9):  # 모두 출력
            print(*data[i])
        flag = True

    if flag:  # 답을 찾으면 return
        return

    # 반복문을 통해 빈칸에 1부터 9까지 넣어본다
    for i in range(1, 10):
        x, y = zero[cnt][0], zero[cnt][1]  # 빈칸의 x좌표, y좌표
        if garo_check(x, i) and sero_check(y, i) and nemo_check(x, y, i):
            data[x][y] = i
            dfs(cnt + 1)  # 다음 빈칸을 계속해서 탐색
            data[x][y] = 0

data = [list(map(int, input().split())) for _ in range(9)]

zero = []

for i in range(9):
    for j in range(9):
        if data[i][j] == 0:
            # 0인곳을 담아주자
            zero.append((i, j))

flag = False
dfs(0)
