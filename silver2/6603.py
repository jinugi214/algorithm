from itertools import combinations

while True:
    data = list(map(int, input().split()))

    k = data[0]
    
    if k == 0:
        break
    
    data = data[1:]

    ans = list(combinations(data, 6))
    for i in ans:
        print(*i)
    print()