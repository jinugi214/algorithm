size = 100

N = int(input())

# 가로, 세로 길이 10 고정
# x, y

data = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        data[i][y:(y+10)] = [1] * 10

ans = 0
for j in range(100):
    ans += data[j].count(1)

print(ans)