list = list(map(int, input().split()))

chess = [1, 1, 2, 2, 2, 8]

result = [0] * len(list)

for i in range(len(list)):
    result[i] = chess[i] - list[i]
    
for i in range(len(list)):
    print(result[i], end=' ')