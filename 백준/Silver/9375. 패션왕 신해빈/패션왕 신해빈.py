t = int(input())

for _ in range(t):
    clothes = dict()
    n = int(input())
    for _ in range(n):
        item, part = input().split()
        clothes.setdefault(part, 0)
        clothes[part] += 1

    ans = 1
    for x in clothes:
        ans *= (clothes[x] + 1) # +1 의상을 착용해도 되고 안해도되기 때문에 (안 입었을 경우를 위해)

    print(ans-1) # 모든 의상 착용하지 않은 경우 제외