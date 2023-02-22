import math

n = (1234456 * 2) + 1

array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
            
def check(a):
    count = 0
    for i in range(a + 1, (2 * a) + 1):
        if array[i] == True:
            count += 1
    return count


while True:
    a = int(input())
    if a == 0:
        break
    elif a == 1:
        print(1)
    else:
        print(check(a))
