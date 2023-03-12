# i-1 -> i -> i+1
#  N 1
# 종이에는 -N <= 정수 <= N

# 1번부터 풍선 터트리며 종이에 적혀있는 값만큼 이동하며
# 양수일 경우 오른쪽 음수일 경우 왼쪽 이동

# 번 풍선의 왼쪽에 N번 풍선이 있고, N번 풍선의 오른쪽에 1번 풍선이 있다.
# -> 원형 큐를 이용한 문제

from collections import deque

N = int(input())

input_data = list(map(int, input().split()))

data = []

for idx, val in enumerate(input_data):
    data.append((idx, val))

idx = 0

q = deque(data)

while q:
    idx, val = q.popleft()
    # 음수를 넣으면 오른쪽 이동, 양수를 넣으면 왼쪽 이동이 된다.
    print(idx + 1, end=' ')
    if val > 0:
        q.rotate(-(val - 1))  # Argument 음수를 넣게 된다면 왼쪽 회전 양수는 오른쪽 회전
    else:
        q.rotate(-val)
