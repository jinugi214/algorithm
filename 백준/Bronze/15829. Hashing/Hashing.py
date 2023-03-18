import string
import sys

input = sys.stdin.readline

L = int(input())
data = list(input())
alpha = string.ascii_lowercase

ans = 0

for i in range(L):
    for j in range(len(alpha)) :
        if data[i] == alpha[j]:
            ans += (j + 1) * 31**i

print(ans)