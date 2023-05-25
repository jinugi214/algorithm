N = int(input())

val = 2
jump = 1
lst = [0] * (N+1)
for i in range(1, N+1):
    val += jump
    lst[i] = val**2
    jump *= 2

print(lst[-1])
