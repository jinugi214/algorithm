from itertools import combinations

L, C = map(int, input().split())
data = list(input().split())

data = sorted(data)

res = list(combinations(data, L))

mo = ['a', 'e', 'i', 'o', 'u']

for i in res:
    cnt = 0
    for j in i:
        if j in mo:
            cnt += 1 
    if 0 < cnt < L - 1:
        print(''.join(i))