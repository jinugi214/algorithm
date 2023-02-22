import sys

n = int(input())

a = map(int, sys.stdin.readline().split())

result = 0

for i in a:
    if i > 1:
        error = 0
        for j in range(2, i):
            if i % j == 0:
                error += 1
        
        if error == 0:
            result += 1
print(result)