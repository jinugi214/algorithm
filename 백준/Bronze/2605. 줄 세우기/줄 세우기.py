N = int(input())

data = list(map(int, input().split()))

line = []

cnt = 1
for i in data:
    line.insert(i, cnt)
    cnt += 1


print(*line[::-1], sep=' ')
