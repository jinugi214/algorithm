from collections import deque

# 원형 큐

N, K = map(int, input().split())

num = 0

data = [i for i in range(1, N + 1)]

q = deque(data)

ans = []
while q:
    q.rotate(-(K - 1)) # 현재자리를 기준으로 돌리기 떄문에 K-1
    ans.append(q.popleft())

print('<', end='')
print(', '.join(map(str, ans)), end='')
print('>')
