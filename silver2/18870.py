import sys

input = sys.stdin.readline

dic = {}

n = int(input())
data = list(map(int, input().split()))

check = list(sorted(set(data)))

for i in range(len(check)):
    dic[check[i]] = i
    
for j in data:
    print(dic[j], end =' ')
