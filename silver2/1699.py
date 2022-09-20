import sys

input = sys.stdin.readline

n = int(input())

dp = [i for i in range(n + 1)]

for i in range(1, n+1):
    for j in range(1,i):
        #제곱수가 i보다 커지면 break
        if (j*j) > i:
            break
        # 4와 같은 새로운 제곱수가 등장할 때 횟수가 1로 초기화된다.
        # 이를 이용하면 밑에와 같은 형식을 가지게 된다.
        # ex) i가 5라면 j는 2까지 loop 돌고 이전 수 2**2에 +1**2을 더하는 방법이기에 횟수 2이다.
        if dp[i] > dp[i-j*j]+1:
            dp[i] = dp[i-j*j] + 1
            
print(dp[n])

