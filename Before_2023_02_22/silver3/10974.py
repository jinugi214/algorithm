from itertools import permutations
import math

n = int(input())

data = []

for i in range(1, n+1):
    data.append(i)

result = list(permutations(data, n))

limit = math.factorial(n)

for i in range(limit):
    print(*result[i])