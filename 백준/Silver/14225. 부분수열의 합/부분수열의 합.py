from itertools import combinations

N = int(input())
S = list(map(int, input().split()))

limit = sum(S)

check = [0] * (limit+2)
check[0] = 1

for i in range(1, len(S)+1):
    num = list(combinations(S, i))
    for j in num:
        idx = sum(j)
        check[idx] = 1

print(check.index(0))