import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 3
for i in range(3, n + 1):
    # dp[i] 일때 dp[i - 1]의 모양은 그대로 가지고있지만, 
    # dp[i - 2]의 경우 2번씩 모양이 들어간다.
    dp[i] = dp[i - 1] + (2 * dp[i - 2])
    
print(dp[n] % 10007)