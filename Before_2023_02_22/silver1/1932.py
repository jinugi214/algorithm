import sys

input = sys.stdin.readline

n = int(input())

d = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(d[i])):
        if j == 0: # 맨 왼쪽
            d[i][j] = d[i-1][j] + d[i][j] 
        elif j == len(d[i]) - 1: # 맨 오른쪽
            d[i][j] = d[i-1][j-1] + d[i][j] 
        else: # 그 외 중앙
            d[i][j] = max(d[i-1][j-1], d[i-1][j]) + d[i][j]

print(max(d[n-1]))