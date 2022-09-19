import sys

n = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(n + 1)]

# 초기값 설정 
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n + 1):
    # 계단 수가 0으로 끝난느 경우
    dp[i][0] = dp[i - 1][1]
    # 계단 수가 9로 끝나는 경우
    dp[i][9] = dp[i - 1][8]
    
    # 계단 수가 1~8로 끝나는 경우
    for j in range(1, 9):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n]) % 1000000000)

'''
어떤 N자리 수의 계단 수가 숫자 M으로 끝난다고 하자.
그렇다면 그 수는 N-1자리 수의 계단 수의 뒤에 숫자 M을 붙인 것과 같다.
그리고 전체 수가 계단 수가 되려면, M 앞의 계단 수는 M-1 또는 M+1로 끝나야 한다.

마지막 자리수에 0이 오게되면 N-1자리에 1만 가능하다.
마지막 자릿수에 9가 오게되면 N-1자리에 8만 가능하다.
'''