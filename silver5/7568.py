# 덩치 = (몸무게, 키)

n = int(input())

data = []

for _ in range(n):
    x, y = list(map(int, input().split()))
    data.append((x, y))
    
for i in data:
    rank = 1
    for j in data:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = ' ')
