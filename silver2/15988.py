import sys

input = sys.stdin.readline

t = int(input())

data = []

for _ in range(t):
    n = int(input())
    data.append(n)
    
dp = [0] * (max(data) + 1)

dp[1] = 1 

dp[2] = 2 

dp[3] = 4 

dp[4] = 7 

for i in range(5, (max(data) + 1)):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])  %  1000000009

for i in range(t):
    print(dp[data[i]])