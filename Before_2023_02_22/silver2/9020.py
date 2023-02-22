import math


def check(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

t = int(input())

for _ in range(t):
    n = int(input())
    
    a, b = n // 2, n // 2
    while a > 0:
        if check(a) and check(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1

