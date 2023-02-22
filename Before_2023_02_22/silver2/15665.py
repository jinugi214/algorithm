from itertools import product

n, m = map(int, input().split())

data = list(map(int, input().split()))

result = list(set(product(data, repeat=m)))

result.sort()

for i in result:
    print(*i)
