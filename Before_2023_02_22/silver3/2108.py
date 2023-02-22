from collections import Counter
import sys

n = int(input())

list = []

for _ in range(n):
    list.append(int(sys.stdin.readline()))
    
# 첫째 줄
print(round(sum(list) / n))

# 둘째 줄
list.sort()
print(list[n // 2])

# 셋째 줄
cnts = Counter(list).most_common(2)

if len(list) > 1:
    if cnts[0][1] == cnts[1][1]:
        print(cnts[1][0])
    else:
        print(cnts[0][0])
else:
    print(cnts[0][0])
    
# 넷째 줄
print(list[-1] - list[0])
