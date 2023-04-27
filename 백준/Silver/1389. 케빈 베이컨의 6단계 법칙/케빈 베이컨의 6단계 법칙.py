import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    nums = [0] * (N+1)
    used = [0] * (N+1)
    q = deque()
    q.append(start)

    while q:
        x = q.popleft()
        for i in data[x]: # 연결된 곳
            if not used[i]: # 방문하지 않은 곳이면
                nums[i] =nums[x] + 1 # 이전 값에서 +1
                used[i] = 1 # 방문처리
                q.append(i)
    return sum(nums)

N, M = map(int, input().split())

data = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split()) # 양방향 연결
    data[a].append(b)
    data[b].append(a)

val = 1e9
for i in range(1, N+1):
    if bfs(i) < val:
        val = bfs(i)
        ans = i

print(ans)
