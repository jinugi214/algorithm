data = list(map(int, input().split()))

val = 0

for i in data:
    val += i**2

ans = val % 10

print(ans)