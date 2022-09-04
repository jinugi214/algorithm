import sys
import math

input = sys.stdin.readline

t = int(input())

nums = [int(input()) for _ in range(t)]

m = max(nums)

prime = [False, False] + [True] * (m - 1)

for i in range(2, int(math.sqrt(m)) + 1):
    if prime[i] == True:
        j = 2
        while i * j <= m:
            prime[i * j] = False
            j += 1
            
for num in nums:
    cnt = 0
    for i in range((num//2)+1):
        if prime[i] and prime[num-i]:
            cnt += 1
    print(cnt)