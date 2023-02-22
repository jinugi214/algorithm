import sys

input = sys.stdin.readline

n = input().rstrip()

two = '0b'

ten = int(two + n, 2)

o = oct(ten)

print(o[2:])