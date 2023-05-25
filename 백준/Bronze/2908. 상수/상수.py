A, B = input().split()
a = ''
b = ''

for i in range(2, -1, -1):
    a += A[i]
    b += B[i]

a = int(a)
b = int(b)

if a >= b:
    print(a)
else:
    print(b)