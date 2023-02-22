import math
import sys

n = 1000000

array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

while True:
    n = int(sys.stdin.readline())

    if n == 0: break

    for i in range(3, len(array)):
        if array[i] and array[n-i]:
            print(n, "=", i, "+", n-i)
            break