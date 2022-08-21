import sys

n = int(sys.stdin.readline())

data = []

for _ in range(n):
    data.append(sys.stdin.readline().strip())

data = set(data)

data = list(data)

data.sort()
data.sort(key=len)

for i in data:
    print(i)