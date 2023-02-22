import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

dp = [[0] * n for _ in range(2)]

dp[0][0] = arr[0] # 1개는 반드시 선택해야 한다.

if n > 1:
    ans = -1e9
    for i in range(1, n):
        # dp[0][i] : 특정 원소를 제거하지 않은 경우
        dp[0][i] = max(arr[i] + dp[0][i - 1], arr[i])
        # dp[1][i] : 특정 원소를 제거한 경우 
        # 1.i번째 원소 제거  2.i번째 전에 원소를 제거하고 i번째 원소를 선택하는 경우
        dp[1][i] = max(dp[0][i - 1], dp[1][i-1] + arr[i])

        ans = max(ans, dp[0][i], dp[1][i])
    print(ans)
else: # n이 0이면 dp[0][0]만 선택가능하다.
    print(dp[0][0])