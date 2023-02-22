import sys

input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))

sum_data = [data[0]]

for i in range(len(data) - 1):
    # 지금까지 더한 수열, 현재 위치 값 중 큰 것을 리스트에 담는다.
    sum_data.append(max(sum_data[i] + data[i + 1], data[i + 1]))

print(max(sum_data))
