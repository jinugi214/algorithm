T = int(input())

for _ in range(T):
    C = int(input())
    q, d, n, p = 0, 0, 0, 0
    q += (C // 25)
    C -= (q * 25)
    d += (C // 10)
    C -= (d * 10)
    n += (C // 5)
    C -= (n * 5)
    p += (C // 1)

    print(q, d, n, p)

