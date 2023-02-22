import sys

input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+1)]

if n <= 3:
    print(n)
else:
    # 2 * 1 크기와 2 * 2 크기를 채우는 방식을 이용해 큰 수를 구해간다.
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[i] % 10007)