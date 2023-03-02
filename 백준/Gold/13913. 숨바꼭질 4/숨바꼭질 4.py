from collections import deque

N, K = map(int, input().split())

MAX = 100001
cnt = [-1] * MAX
move = [-1] * MAX

q = deque()

q.append(N)
cnt[N] = 0

cnt_ans = 0

while q:
    val = q.popleft()
    if val == K:
        cnt_ans = cnt[K]
        break

    for x in (val * 2, val + 1, val - 1):
        if 0 <= x < MAX and cnt[x] == -1:
            cnt[x] = cnt[val] + 1
            move[x] = val
            q.append(x)

cnt_lst = [K]

for _ in range(cnt_ans):
    cnt_lst.append(move[cnt_lst[-1]])

print(cnt_ans)
print(*cnt_lst[::-1], sep=' ')