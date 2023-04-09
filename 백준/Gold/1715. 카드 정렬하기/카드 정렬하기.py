from heapq import heappush, heappop
import sys

input = sys.stdin.readline

cards = [] # 카드를 담아주는 곳
result = 0 # 총 비교횟수

for i in range(int(input())):
    heappush(cards, int(input())) # 카드를 담아주자

if len(cards) == 1:
    print(0) # 카드가 하나면 비교를 하지 않는다.
else:
    while len(cards) > 1: # 최소힙을 이용해 비교횟수를 계속해서 추가해주자
        # 카드 장수가 가장 적은 두 카드들을 서로 비교하자
        plus = heappop(cards) + heappop(cards)
        result += plus # 총 비교횟수에 추가
        heappush(cards, plus) # 서로 비교한 카드를 다시 담아주자

    print(result)
