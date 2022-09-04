import sys

input = sys.stdin.readline

n = int(input())

d = [0] * (n + 1)

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1 # 뒤에 + 1은 계산 횟수 저장을 위해
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1) # 뒤에 + 1은 계산 횟수 저장을 위해
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1) # 뒤에 + 1은 계산 횟수 저장을 위해
print(d[n])