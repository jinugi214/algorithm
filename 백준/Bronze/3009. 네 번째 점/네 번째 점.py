a_lst = []
b_lst = []

for _ in range(3):
    a, b = map(int, input().split())
    if a in a_lst:
        a_lst.remove(a)
    else:
        a_lst.append(a)
    if b in b_lst:
        b_lst.remove(b)
    else:
        b_lst.append(b)

print(a_lst[0], b_lst[0])
