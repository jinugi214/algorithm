import sys

input = sys.stdin.readline

n = int(input())

data = []


for _ in range(n):
    data.append(list(map(int, input().rstrip().split())))

for i in range(1, n):
    # 빨강
    data[i][0] = min(data[i - 1][1], data[i - 1][2]) + data[i][0]
    # 파랑
    data[i][1] = min(data[i - 1][0], data[i - 1][2]) + data[i][1]
    # 초록
    data[i][2] = min(data[i - 1][0], data[i - 1][1]) + data[i][2]

print(min(data[n - 1])) # 인덱스가 0부터 시작했기에 (n - 1)


'''
두번째 값부터 현재 i의 색깔을 제외한 (i - 1) 중에서
최솟값을 구해 현재 값을 더해서 현재 값을 갱신한다. 

ex) 현재 집에 파랑색깔을 칠한다고 가정하면
전의 집에 파랑을 제외한 빨강, 초록의 비용 중
최솟값을 구해 현재의 파랑색깔 비용을 더해
현재 값을 지금까지 총 비용으로 갱신한다.

'''