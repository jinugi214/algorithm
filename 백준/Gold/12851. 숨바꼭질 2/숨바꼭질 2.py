from collections import deque

N, K = map(int, input().split())

MAX = 100001
time = [-1] * MAX
num = [0] * MAX

q = deque()

q.append(N)
time[N] = 0

while q:
    val = q.popleft()
    if val == K:
        print(time[K])
        if num[K] == 0:
            print(1)
        else:
            print(num[K])
        break

    for x in (val * 2, val + 1, val - 1):
        if 0 <= x < MAX and time[x] == -1:
            time[x] = time[val] + 1
            num[x] = 1
            q.append(x)

        elif 0 <= x < MAX and time[x] != -1:
            if time[x] == time[val] + 1:
                num[x] += 1
                q.append(x)
