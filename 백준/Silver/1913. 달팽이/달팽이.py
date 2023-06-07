n = int(input())
f = int(input())
data = [[0] * n for _ in range(n)]

# 1이 위치할 중앙 위치 찾기
# n이 홀수이면 x, y 는 같지만 짝수이면 x값이 y보다 1 더 크다.
if n % 2 == 0:
    x = n // 2
    y = x - 1
else:
    x = n // 2
    y = x

val = 1
move = 0 # 상, 우, 하, 좌
limit = 1
cnt = 0 # 이동횟수
ans_x, ans_y = 0, 0
while True:
    data[x][y] = val
    if val == f:
        ans_x = x
        ans_y = y
    if val == n**2:
        break
    # 상, 우 같은 값 / 하, 좌 같은 값
    if move == 0:
        x -= 1
    elif move == 1:
        y += 1
    elif move == 2:
        x += 1
    elif move == 3:
        y -= 1
    cnt += 1
    if limit == cnt:
        if move == 1 or move == 3:
            limit += 1
        move += 1
        if move == 4:
            move = 0
        cnt = 0
    val += 1

for i in range(n):
    print(*data[i])

print(ans_x+1, ans_y+1)