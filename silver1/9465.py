import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(2) ]
    
    if n > 1:   # 점화식에 i-2가 있기때문에 처음 값은 직접 더해준다. 
        data[0][1] += data[1][0]
        data[1][1] += data[0][0]
        for i in range(2, n):
            # 선택할 수 있는 두자리에 있는 점수 중, 큰 점수와 현재 스티커와 더해주기
            data[0][i] += max(data[1][i-2], data[1][i-1])
            data[1][i] += max(data[0][i-2], data[0][i-1])
    
    print(max(data[0][-1], data[1][-1])) # 마지막 자리에서 여태까지 더한 제일 큰 점수 선택
