N, M = map(int, input().split())

ball = [0] + [i for i in range(1, N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    ball[a], ball[b] = ball[b], ball[a]

print(*ball[1:])