N = int(input())

data = list(map(int, input().split()))

data.sort()

ans = 0
for i in range(N):
    for j in range(i+1):
        ans += data[j]

print(ans)
