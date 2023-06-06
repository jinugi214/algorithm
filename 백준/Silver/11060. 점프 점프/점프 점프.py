n = int(input())
data = list(map(int, input().split()))

dp = [0] * n
idx = 0
while True:
    if idx >= n - 1:
        break
    val = data[idx]
    for i in range(1, val + 1):
        if idx + i >= n:
            break
        else:
            if idx > 0 and dp[idx] == 0:
                continue
            if dp[idx + i] == 0:
                dp[idx + i] = dp[idx] + 1
    idx += 1

if dp[-1] == 0 and len(data) > 1:
    print(-1)
else:
    print(dp[-1])
