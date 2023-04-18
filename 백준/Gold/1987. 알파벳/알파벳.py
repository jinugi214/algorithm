# dfs사용 pypy3 통과 python3 시간초과
'''
import sys

input = sys.stdin.readline

def dfs(x, y, cnt):
    # Backtracking


    global ans
    alpha[ord(data[x][y]) - 65] = 1
    # 동서남북
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = x + dx, y + dy
        if 0<=nx<R and 0<=ny<C:
            if not alpha[ord(data[nx][ny]) - 65]:
                dfs(nx, ny, cnt+1)
                alpha[ord(data[nx][ny]) - 65] = 0
    else:

        if ans < cnt:
            ans = cnt

R, C = map(int, input().split())

data = [list(input()) for _ in range(R)]

# 본인 칸 포함
ans = 0

# 65~90 A~Z
alpha = [0] * 26

dfs(0, 0, 1)

print(ans)
'''

# bfs set활용 python3 통과
import sys

input = sys.stdin.readline


def bfs(x, y):
    global ans
    q = set([(x, y, data[x][y])])
    while q:
        x, y, val = q.pop()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                if data[nx][ny] not in val:  # 없는 알파벳이면
                    q.add((nx, ny, val + data[nx][ny]))  # 알파벳을 이전 알파벳들과 함께 달아준다.
        else:
            ans = max(ans, len(val))


R, C = map(int, input().split())

data = [list(input()) for _ in range(R)]

# 결과값 담아주는 곳
ans = 0

bfs(0, 0)

print(ans)
