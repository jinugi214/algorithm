import sys 
n = int(sys.stdin.readline())

list = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    list.append((x, y))


list.sort(key=lambda x : (x[1], x[0]))

for i in list:
    x, y = i
    print(x, y)