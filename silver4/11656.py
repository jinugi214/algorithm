import sys

input = sys.stdin.readline

s = input().rstrip()

data = []

for i in range (len(s)):
    data.append(s[i:])
    
data.sort()

for i in range(len(data)):
    print(data[i])