import sys

input = sys.stdin.readline

N = int(input())

stairs = [int(input()) for _ in range(N)]

dp = [0] * N

# 연속 세개 X
# +3 칸 이동 X

# dp를 이용해 각 구간 별 최댓값을 설정해주기

if len(stairs) <= 2:
    print(sum(stairs))
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    for i in range(2, N):
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    print(dp[-1])
