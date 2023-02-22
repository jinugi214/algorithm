# 카드개수가 적으면서 비싼 카드 위주로 산다.
# 원하는 카드개수보다 많이 사는 것은 불가
import sys

input = sys.stdin.readline

n = int(input())

p = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + p[j]) 
        
print(dp[n])

'''
d[2] = d[1] + p[1] or d[0] + p[2]

d[3] = d[2] + p[1] or d[1] + p[2] or d[0] + p[3]

d[4] = d[3] + p[1] or d[2] + p[2] or d[1] + p[3] or d[0] + p[4]

모든 경우의 수를 계산해서 최댓값을 구하자
'''