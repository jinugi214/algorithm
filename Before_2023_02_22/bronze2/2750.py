n = int(input())

list = []

for _ in range(n):
    list.append(int(input()))

list.sort()

for i in range(n):
    print(list[i])