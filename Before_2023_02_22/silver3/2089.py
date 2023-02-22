import sys

input = sys.stdin.readline

n = int(input())

if not n:
    print('0')
    exit()
res =''
while n:
    if n % (-2):
        res = '1' + res
        n = n // -2 + 1
    else:
        res ='0' + res
        n = n // -2

print(res)
    