import sys

input = sys.stdin.readline

N = int(input())

size = [[0] * 1001 for _ in range(1001)]

max_w = 0
max_h = 0

for x in range(1, N + 1):
    a, b, w, h = map(int, input().split())
    max_w = max(max_w, a + a + w)
    max_h = max(max_h, b + b + h)
    for i in range(a, a + w):
        for j in range(b, b + h):
            size[i][j] = x

for x in range(1, N + 1):
    rlt = 0
    for i in range(max_w):
        for j in range(max_h):
            if size[i][j] == x:
                rlt += 1
    print(rlt)
