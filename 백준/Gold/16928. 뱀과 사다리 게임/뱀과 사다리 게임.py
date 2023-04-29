import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque([1])
    while q:
        x = q.popleft()

        for i in range(1, 7):
            nx = x + i

            if nx > 100:
                continue

            jump = move[nx]

            if not visited[jump]:
                q.append(jump)
                visited[jump] = visited[x] + 1

                if jump == 100:
                    return

N, M = map(int, input().split())

NM = N + M
move = [i for i in range(101)]
visited = [0] * 101
for _ in range(NM):
    x, y = map(int, input().split())
    move[x] = y

bfs()

print(visited[100])