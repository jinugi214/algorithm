import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline

# 랜선의 개수와 필요한 랜선의 개수
K, N = map(int, input().split())

# 가지고있는 랜선 입력
data = [int(input()) for _ in range(K)]

def binary_search(start, end):
    mid = (start + end) // 2

    if start > end:
        return mid

    cnt = sum([x // mid for x in data])

    if cnt < N:
        return binary_search(start, mid - 1)
    else:
        return binary_search(mid + 1, end)


print(binary_search(1, max(data)))
