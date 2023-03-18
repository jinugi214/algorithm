N = int(input())

N_data = list(map(int, input().split()))

M = int(input())

M_data = list(map(int, input().split()))

dict = {}

for i in N_data:
    if dict.get(i) is None:
        dict[i] = 1
    else:
        dict[i] += 1

for i in M_data:
    if dict.get(i) is not None:
        print(dict[i], end=' ')
    else:
        print(0, end=' ')
