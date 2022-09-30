import sys

input = sys.stdin.readline

n = int(input())

data = [0] * (n + 1)

# 사자 한 마리도 배치하지 않는 경우의 수 포함
data[0] = 1
data[1] = 3

for i in range(2, n + 1):
    data[i] = (data[i-2] + (data[i-1]*2)) % 9901

print(data[n])

'''
i-1칸에 사자가 있는 경우 i칸에 빈 우리 혹은 대각선 반대 방향으로 둘 수 있다.
(dp[i-1] - dp[i-2]) * 2


i-1칸에 사자가 없는 경우 i칸에 3가지 수 아무거나 가능하다.
dp[i-2] * 3


'''