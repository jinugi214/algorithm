import sys

input = sys.stdin.readline

# 동생 수 n, 수빈이 현재 점 s
n, s = map(int, input().split())

# 동생 수에 맞는 동생의 위치
data = list(map(int, input().split()))

def gcm(a, b):
    while b>0:
        a, b = b, a % b
    return a

data.append(s)

data.sort()

distance = []

for i in range(1, len(data)):
    distance.append(data[i] - data[i - 1])

result = distance.pop()

while distance:
    tmp = distance.pop()
    result = gcm(result, tmp)

print(result)