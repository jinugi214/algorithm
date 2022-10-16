import sys

input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    dp[i] = data[i]

for i in range(1, n):
    for j in range(i):    
        if data[i] > data[j]:
            dp[i] = max(data[i] + dp[j], dp[i])

print(max(dp))