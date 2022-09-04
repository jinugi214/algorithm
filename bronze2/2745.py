import sys
import string

input = sys.stdin.readline

n, b = input().split()

b = int(b)

temp = string.digits + string.ascii_uppercase

now = 0

for i in range(len(n)):
    res = temp.index(n[i])
    now = now * b + res

print(now)