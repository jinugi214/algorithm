a, b, c = map(int, input().split())

lst = [a, b, c]
v1 = min(lst)
lst.remove(v1)
v2 = min(lst)
v3 = max(lst)
if v1 + v2 > v3:
    print(v1 + v2 + v3)
else:
    print((v1 + v2) * 2 - 1)

