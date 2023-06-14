N = int(input())

if N == 0:
    print(1)
else:
    rlt = 1
    for i in range(N, 0, -1):
        rlt *= i
    print(rlt)