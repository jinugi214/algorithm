from itertools import product

n, m = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

result = list(product(data, repeat = m))

for i in result:
    print(*i)