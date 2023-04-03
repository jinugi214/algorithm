import sys

input = sys.stdin.readline

N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]


def check(x, y, N):
    global white, blue
    color = data[x][y] # 현재 색종이 대표 색깔
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != data[i][j]: # 대표색깔과 다르면 4구간으로 잘라야한다.
                check(x, y, N // 2) # I 구간
                check(x, y + N // 2, N // 2) # II 구간
                check(x + N // 2, y, N // 2) # III 구간
                check(x + N // 2, y + N // 2, N // 2) # IV 구간
                return
    # 대표색깔과 색이 같으면 색종이 개수에 포함시켜주자
    if color == 0:
        white += 1
    else:
        blue += 1


white = 0
blue = 0

check(0, 0, N)

print(white)
print(blue)
