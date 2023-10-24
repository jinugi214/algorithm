n, m = map(int, input().split())

pack = []
each = []

# 6개가 들은 패키지 가격, 낱개 가격
for _ in range(m):
    p, e = map(int, input().split())
    pack.append(p)
    each.append(e)

price = 0
mp, me = min(pack), min(each)
while n > 0:
    if n >= 6:
        if (mp // 6) < me:
            n -= 6
            price += mp
        else:
            n -= 1
            price += me
    else:
        if mp > (me * n):
            price += me * n
            n = 0
        else:
            price += mp
            n = 0

print(price)