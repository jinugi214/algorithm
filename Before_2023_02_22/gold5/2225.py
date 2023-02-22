import sys
from itertools import combinations

input = sys.stdin.readline

n, k = map(int, input().split())

dp = [ [i] * 201 for i in range(201)]


# k = 2 이면 합이 n이 되는 경우의 수는 n + 1개다.
for i in range(201):
    dp[1][i] = 1
    dp[2][i] = i + 1

#(i, j 2이상인 경우) dp[i][j] = dp[i][j-1]+dp[i-1][j] 점화식 규칙이 있다.
for i in range(2, 201):
    dp[i][1] = i
    for j in range(2, 201):
        dp[i][j] = (dp[i][j-1]+dp[i-1][j]) % 1000000000

print(dp[k][n])
