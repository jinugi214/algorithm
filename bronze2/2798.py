from itertools import combinations

n, m = map(int, input().split())

data = list(map(int, input().split()))

result = list(combinations(data, 3))

max_result = 0

for i in range(len(result)):
    if sum(result[i]) <= m:
        max_result = max(max_result, sum(result[i]))

print(max_result)