import sys

input = sys.stdin.readline

T = int(input())

data = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(10, 101):
    data.append(data[i-1] + data[i-2])

for t in range(T):
    N = int(input())
    print(data[N])
