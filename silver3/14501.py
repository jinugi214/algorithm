N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    if i + data[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], data[i][1] + dp[i + data[i][0]])

print(dp[0])