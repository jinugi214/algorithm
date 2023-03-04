N = int(input())

data = list(map(int, input().split()))

up_cnt = 1
down_cnt = 1
max_up = 0
max_down = 0
for i in range(N - 1):
    if data[i] < data[i + 1]:
        up_cnt += 1
        max_down = max(max_down, down_cnt)
        down_cnt = 1
    elif data[i] > data[i + 1]:
        down_cnt += 1
        max_up = max(max_up, up_cnt)
        up_cnt = 1
    else:
        up_cnt += 1
        down_cnt += 1

max_down = max(max_down, down_cnt) # 인덱스가 끝까지 도착했을 경우를 위해
max_up = max(max_up, up_cnt)

print(max(max_up, max_down))
