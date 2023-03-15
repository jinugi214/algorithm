import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
for i in range(N):
    arr[i] = (i+1, arr[i])
idx = 0
ans = []
while True:
    temp = arr.pop(idx)
    ans.append(temp[0])
    next = temp[1]-1    
    N -= 1
    if N == 0:
        break
    if next < 0:
        next += N+1
    idx = (idx+next)%N    
print(*ans)