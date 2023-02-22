m = int(input())
n = int(input())

result = []

for i in range(m, n + 1):
    if i != 1:
        check = True
        for j in range(2, i):
            if i % j == 0 and i != j:
                check = False
                break
        if check:
            result.append(i)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))