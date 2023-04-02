from heapq import heappop, heappush
import sys

input = sys.stdin.readline

N = int(input())

heap = []

for i in range(N):
    val = int(input())
    if val == 0:
        if heap:
            print(-heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, -val)
