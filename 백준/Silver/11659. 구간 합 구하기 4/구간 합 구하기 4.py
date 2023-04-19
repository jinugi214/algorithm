import sys

input = sys.stdin.readline

N, M = map(int, input().split())

data = list(map(int, input().split()))

sum_lst = [0] * (N + 1)

for i in range(N):
    sum_lst[i+1] = sum_lst[i] + data[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_lst[j] - sum_lst[i-1])
