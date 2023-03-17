import sys
input = sys.stdin.readline

def isBig(a, b):
    if a[0] < b[0] and a[1] < b[1]:
        return True
    return False

N = int(input())
arr = []
ans = [1]*N
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if isBig(arr[i], arr[j]):
            ans[i] += 1
print(*ans)