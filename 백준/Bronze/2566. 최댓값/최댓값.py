data = [list(map(int, input().split())) for _ in range(9)]

mv = 0
mi = 0
mj = 0

for i in range(9):
    for j in range(9):
        if data[i][j] > mv:
            mi = i
            mj = j
            mv = data[i][j]
print(mv)
print(mi+1, mj+1)