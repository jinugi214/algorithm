import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)

# 모든 홀수의 경우의 수는 0이다.
if n % 2 != 0:
    print(0)
else:
    dp[2] = 3
    for i in range(4, n+1, 2):
        # 끝에 2칸만의 3가지 경우의 수와 짝수 n일 경우 고유 모양 2개씩 추가된다.
        dp[i] = dp[i - 2] * 3 + 2  
        for j in range(2, i - 2, 2): 
            # 2칸 간격으로 고유 모양이 2가지씩 추가되기 때문에 * 2를 한다.
            dp[i] += dp[j] * 2
    print(dp[n])