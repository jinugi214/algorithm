# sort를 사용하면 메모리 초과가 나온다.

import sys

n = int(input())

num = [0] * 10001

for _ in range(n):
    temp = int(sys.stdin.readline())
    num[temp] += 1

for i in range(10001):
    if num[i] != 0:
        for j in range(num[i]):
            print(i)