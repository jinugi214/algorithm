n, k = map(int, input().split())

lst = []

for i in range(1, n+1):
    if not n % i:
        lst.append(i)

if not lst:
    print(0)
elif len(lst) < k:
    print(0)
else:
    print(lst[k-1])
