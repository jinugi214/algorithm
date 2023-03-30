import sys

input = sys.stdin.readline

N = int(input())

ans = 0
row = [0] * N


def check(x):
    for i in range(x):
        # 그전에 퀸이 같은 행에 있거나 또는 대각선에 있으면
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def queens(x):
    global ans
    if x == N:  # N개 퀸 다 놓았을 때
        ans += 1
        return

    else:
        for y in range(N):
            row[x] = y  # 해당 x행, y열에 퀸을 놓아보자 (x, y)
            if check(x):  # 놓을 수 있으면
                queens(x + 1)  # 다음 행에도 퀸을 놓으러 가자


queens(0)
print(ans)
