import sys
import math

n = int(sys.stdin.readline())
    
count = 0

for x in str(math.factorial(n))[::-1]:
    if x == '0':
        count += 1
    else:
        break

print(count)