n, m = map(int, input().split())

# nPm // m!

val = 1
for i in range(n, n-m, -1):
    val *= i

div = 1
for i in range(m, 0, -1):
    div *= i

print(val // div)