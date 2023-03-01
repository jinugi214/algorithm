from collections import deque
limit = 100001
cnt = [0] * limit

N, K = map(int, input().split())

q = deque()
q.append(N)

cnt[N] = 1

while q:
    val = q.popleft()
    if val == K:
        print(cnt[K] - 1) # 원래 0초에서 시작하기 때문에 1 빼준다
        break

    for x in (2 * val, val - 1, val + 1): # 이동
        if 0 <= x < limit and not cnt[x]: # 방문안한 곳인지 확인
            if x == 2 * val: # 순간이동이면
                cnt[x] = cnt[val] # 시간변화 없음
                q.append(x)
            else:
                cnt[x] = cnt[val] + 1 # 걸으면 1초
                q.append(x)
