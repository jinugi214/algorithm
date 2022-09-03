import sys

input = sys.stdin.readline

n = input().rstrip()

eight = '0o'

ten = int(eight + n, 8)

b = bin(ten)

print(b[2:])