import sys

n = int(sys.stdin.readline())

data = []

for i in range(1, n + 1):
    age, name = sys.stdin.readline().split()
    data.append((int(age), name, i))

data.sort(key = lambda x : (x[0], x[2]))

for i in range(n):
    print("%d %s"%(data[i][0], data[i][1]))