import sys
input = sys.stdin.readline

t = int(input())

# 규칙을 1차원이 아닌 2차원으로 생각하기
dp = [[0 for _ in range(3)] for i in range(100001)]

div = 1000000009

# [n]값을 만들기 위해 총 [1, 2, 3]의 사용횟수
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100001):
    # n이 만약 6인 상황에서
    
    # dp[5]에서 2로 끝난거 +1을 해주거나, 3으로 끝난거에 +1을 해주면 -> dp[6][0]
    dp[i][0]=(dp[i-1][1]+dp[i-1][2]) %div
    # dp[4]에서 1로 끝난거에 +2 or 3으로 끝난거에 +2 -> dp[6][1]
    dp[i][1]=(dp[i-2][0]+dp[i-2][2]) %div
    # dp[3]에서 1 or 2로 끝난거에 +3 을 해주면 -> dp[6][2]
    dp[i][2]=(dp[i-3][0]+dp[i-3][1]) %div
    

for _ in range(t):
    n = int(input())
    print(sum(dp[n]) % div )
