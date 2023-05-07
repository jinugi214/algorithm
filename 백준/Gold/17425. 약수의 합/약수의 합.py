# A = BC
# B와 C는 A의 약수이다.
# A는 B와 C의 배수이다.

limit = 1000000 # 최대 값

dp = [0] * (limit + 1) # 각 인덱스별 약수의 합
vals = [0] * (limit + 1) # 각 인덱스까지의 누적합

for i in range(1, limit + 1):
    j = 1
    while i * j <= limit:
        dp[i * j] += i # i의 배수에 속하는 인덱스에 i를 모두 더해준다.
        j += 1
    vals[i] = vals[i-1] + dp[i] # 이전까지의 누적합과 현재 합을 더해주면 된다.

T = int(input())

rlt = []
for _ in range(T):
    N = int(input())
    rlt.append(vals[N])

print(*rlt, sep="\n")