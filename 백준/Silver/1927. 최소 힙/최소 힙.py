from heapq import heappush, heappop
import sys

input = sys.stdin.readline

N = int(input())

heap = []
for _ in range(N):

    val = int(input())
    if val == 0:
        if heap:
            print(heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, val)
