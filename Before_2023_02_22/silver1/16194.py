import sys

input = sys.stdin.readline

n = int(input())

p = [0] + list(map(int, input().split()))

dp = [1e9] * (n + 1)

dp[0] = 0
dp[1] = p[1]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = min(dp[i], dp[i - j] + p[j]) 

print(dp[n])

'''
d[2] = d[1] + p[1] or d[0] + p[2]

d[3] = d[2] + p[1] or d[1] + p[2] or d[0] + p[3]

d[4] = d[3] + p[1] or d[2] + p[2] or d[1] + p[3] or d[0] + p[4]

모든 경우의 수를 계산해서 최솟값을 구하자
'''