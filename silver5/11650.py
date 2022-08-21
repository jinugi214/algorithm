n = int(input())

list = []

for _ in range(n):
    x, y = map(int, input().split())
    list.append((x, y))
    
list.sort()

for i in list:
    x, y = i
    print(x, y)