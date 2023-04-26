from heapq import heappop, heappush
import sys

input = sys.stdin.readline

N = int(input())
h = []
for _ in range(N):
    x = int(input())
    if x != 0:
        if x < 0:
            heappush(h, (abs(x), -1))
        else:
            heappush(h, (x, 1))
    elif x == 0:
        if h:
            v = heappop(h)
            print(v[0] * v[1])
        else:
            print(0)