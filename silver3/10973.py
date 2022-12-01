n = int(input())

input = list(map(int, input().split()))

for i in range(n-1, 0, -1): # 마지막 항 부터 확인
    if input[i-1] > input[i]: # 만약 얖 열의 값이 그 뒷열의 값보다 크다면
        for j in range(n-1, 0, -1): # 다시 그 앞 열의 값을 맨 뒷열부터 비교
            if input[i-1] > input[j]: # 그 앞열의 값이 뒤에 있는 어느 열보다 크다면
                input[i-1], input[j] = input[j], input[i-1] # 그 두 값을 스왑
                input = input[:i] + sorted(input[i:], reverse=True)
                print(*input)
                exit()

print(-1)