H, W, X, Y = map(int, input().split())

data = [list(map(int, input().split())) for i in range(H+X)]

for i in range(X, H):
    for j in range(Y, W):
        data[i][j] = data[i][j] - data[i-X][j-Y]

for i in range(H):
    print(*data[i][:W])