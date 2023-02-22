import sys

input = sys.stdin.readline

e, s, m = map(int, input().split())

check = 0

a, b, c = 1, 1, 1

cnt = 0

while check != 1:    
    if a == e and b == s and c == m:
        check = 1 
        
    a += 1
    b += 1
    c += 1

    if a > 15:
        a = 1
    if b > 28:
        b = 1
    if c > 19:
        c = 1
        
    cnt += 1
    
print(cnt)