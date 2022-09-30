import sys
from itertools import combinations 


input = sys.stdin.readline

data = []

for i in range(9):
    data.append(int(input()))

result = list(combinations(data, 7))

for i in result:
    if sum(i) == 100:
        i = tuple(sorted(i, key=lambda x: x))
        for x in i:
            print(x)
        break


