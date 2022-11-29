from itertools import permutations

n, m = map(int, input().split())

data = list(map(int, input().split()))

result = list(set(permutations(data, m)))

result.sort()

for i in result:
    print(*i)
