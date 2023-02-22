import sys

input = sys.stdin.readline

n = int(input())

dp = [[0, 0] for _ in range(n + 1)]

# 마지막 숫자개수 0과 1
dp[1] = [0, 1]

for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
    dp[i][1] = dp[i - 1][0]

print(sum(dp[n]))

# 앞자리에 0이면 뒤에 0과 1 둘다 가능하다 -> 0은  [1, 1] 2가지 경우
# 앞자리에 1이면 뒤에 1은 추가 불가능 0만 추가 가능 -> 1은 [1, 0] 1가지 경우
