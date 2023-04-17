n = int(input())

dp = [0, 1]

for i in range(2, n+1):
    min_v = 1e9
    for j in range(1, int(i**(1/2) + 1)):
        # 현재 값보다 작은 값들 중에서 현재값 - 작은값 제곱을 했을 때 최소횟수 찾기
        min_v = min(min_v, dp[i - (j**2)])
    dp.append(min_v + 1) # 방금 경우를 포함해서 + 1
print(dp[n])