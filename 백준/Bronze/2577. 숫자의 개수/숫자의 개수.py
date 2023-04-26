lst = [int(input()) for _ in range(3)]

num = lst[0] * lst[1] * lst[2]

data = list(str(num))
cnt = [0] * 10

for i in data:
    for j in range(11):
        if int(i) == j:
            cnt[j] += 1
            break

for i in cnt:
    print(i)