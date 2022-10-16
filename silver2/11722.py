import sys

input = sys.stdin.readline

n = int(input())

d = list(map(int, input().split()))

dp = [1] * n

for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if d[i] > d[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))