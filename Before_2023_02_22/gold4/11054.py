import sys

input = sys.stdin.readline

n = int(input())

d = list(map(int, input().split()))

# 증가 dp + 감소 dp 했을 때 가장 큰 위치 출력

dp_a = [1] * n

for i in range(n):
    for j in range(i):
        if d[i] > d[j]:
            dp_a[i] = max(dp_a[j] + 1, dp_a[i])

dp_b = [1] * n

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if d[i] > d[j]:
            dp_b[i] = max(dp_b[j] + 1, dp_b[i])

result = [0] * n

for i in range(n):
    result[i] = (dp_a[i] + dp_b[i] - 1)

print(max(result))