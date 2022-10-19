import sys

input = sys.stdin.readline

d = [list(map(int, input().split())) for _ in range(4)]

max_v = 0

for i in range(4):
    if max_v < max(d[i]):
        max_v = max(d[i])

a = [[0] * (max_v + 1) for _ in range(max_v + 1)]

for i in range(4):
    x1, y1, x2, y2 = d[i]
    for x in range(x1, x2):
        for y in range(y1, y2):
            a[x][y] = 1

ans = 0

for i in range(max_v + 1):
    ans += sum(a[i])

print(ans)