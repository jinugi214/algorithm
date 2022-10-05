import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))


for i in range(n - 1, 0, -1): # 마지막 인덱스부터 시작 (오름차순으로 이루어진 순열이기 때문에)
    if data[i - 1] < data[i]: # 만약 앞 열의 값이 그 뒷열의 값보다 작다면
        for j in range(n - 1, 0, -1): # 앞 열의 값을 맨 뒷열부터 비교
            if data[i - 1] < data[j]: # 앞 열의 값이 뒤에 있는 어느 열보다 작다면
                data[i - 1], data[j] = data[j], data[i - 1] # 그 두 값을 스왑
                data = data[:i] + sorted(data[i:]) # 스왑한 앞 열까지 제외하고 그 뒤에 값들을 정렬한 채로 붙인다.
                print(*data)
                exit()

print(-1)