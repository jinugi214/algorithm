T = int(input())

def factorial(x):
    if x == 0:
        return 1
    for n in range(x-1, 1, -1):
        x *= n
    return x

for _ in range(T):
    N, M = map(int, input().split()) # nCm
    # nCr = n! / (n-r)! * r!
    rlt = factorial(M) / (factorial(M-N) * factorial(N))
    print(int(rlt))