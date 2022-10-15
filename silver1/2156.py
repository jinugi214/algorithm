import sys

input = sys.stdin.readline

n = int(input())

data = [0] * 10000

for i in range(n):
    data[i] = int(input())

dp = [0] * 10000

dp[0] = data[0]
dp[1] = data[0] + data[1]
dp[2] = max(data[2] + data[0], data[2] + data[1], dp[1])

for i in range(3, n):
    dp[i] = max(data[i] + dp[i-2], data[i] + data[i-1] + dp[i-3], dp[i-1])
    # dp[i-1]은 현재 와인을 마시지 않는 경우
print(max(dp))