import sys

input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))

dp = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if data[i] > data[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
    
print(max(dp))

'''
6
10 20 10 30 20 50

'''