n = int(input())

dp = [1] * 10

for i in range(1, n):
    for j in range(1, 10):
        dp[j] += dp[j - 1]

print(sum(dp) % 10007)

'''
맨 뒷자리수를 기준으로 기준을 찾으면
i - 1길이의 맨 뒷자리수(j)에
현재 i 길이의 맨 뒷자리수(j-1)를 더하면
현재 i 길이의 맨 뒷자리수 j가 나온다.


'''