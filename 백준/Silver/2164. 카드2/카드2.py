from collections import deque

N = int(input())

data = [i for i in range(1, N+1)]

q = deque(data)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())


print(q[0])