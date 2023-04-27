import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
data = input()

# 반복문을 순회하면서 발견되면 인덱스 옮기기

ex = 'IO' * N + 'I'
n = len(ex)
idx = 0
cnt = 0
for i in range(len(data)-n):
    if data[i:i+n] == ex:
        cnt+=1
print(cnt)