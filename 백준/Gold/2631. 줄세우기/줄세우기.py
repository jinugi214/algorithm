# https://www.acmicpc.net/problem/2631

# 가장 증가하는 수열을 제외하고 나머지를 바꿔주면 되기 때문에
# 수열을 찾아 전체 숫자 개수에서 빼주자

N = int(input())

lst = [0]
for _ in range(N):
    lst.append(int(input()))

dp = [1] * (N + 1)

for i in range(1, N+1):
    for j in range(1, i):
        if lst[j]< lst[i]:
            dp[i] = max(dp[i], dp[j] + 1)


print(N-max(dp))