import sys

input = sys.stdin.readline

n = int(input())

val = 0
for i in range(1, n+1):
    val += (n//i)*i

print(val)