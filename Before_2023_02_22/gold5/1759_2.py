L, C = map(int, input().split())
data = list(input().split())

def combination(arr, r):
    arr = sorted(arr)
    res = []

    def generate(chosen):
        if len(chosen) == r:
            res.append(list(chosen))
            return
        
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])
    return res

ans = combination(data, L)

mo = ['a', 'e', 'i', 'o', 'u']

for i in ans:
    cnt = 0
    for j in i:
        if j in mo:
            cnt += 1 
    if 0 < cnt < L - 1:
        print(''.join(i))