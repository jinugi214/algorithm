from heapq import heappush, heappop
import sys

input = sys.stdin.readline

cards = []
result = 0

for i in range(int(input())):
    heappush(cards, int(input()))

if len(cards) == 1:
    print(0)
else:
    while len(cards) > 1:
        plus = heappop(cards) + heappop(cards)
        result += plus
        heappush(cards, plus)

    print(result)