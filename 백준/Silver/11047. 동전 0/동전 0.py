import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coin = [int(input()) for _ in range(N)]

ans = 0
for i in range(N-1, -1, -1):
    if coin[i] > K:
        continue
    cnt = K // coin[i]
    ans += cnt
    K -= coin[i] * cnt

    if K == 0:
        break

print(ans)
