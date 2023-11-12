# https://www.acmicpc.net/problem/1963
from collections import deque


# 소수 판단
def checkPrime():
    for i in range(2, 100):
        if prime[i]: # 소수의 배수들은 소수가 아니다.
            for j in range(2 * i, 10000, i):
                prime[j] = 0


def bfs(start, end):
    visited = [0] * 10000
    visited[start] = 1
    q = deque()
    q.append((start, 0))
    while q:
        x, cnt = q.popleft()

        if x == end:
            return cnt

        nx = str(x)

        for i in range(4):
            # 각 자리마다 0~9 숫자 넣어보기
            for j in range(10):
                tmp = int(nx[:i] + str(j) + nx[i + 1:])
                # 방문 안했고 소수이며 1000이상이면
                if not visited[tmp] and prime[tmp] and tmp >= 1000:
                    visited[tmp] = 1
                    q.append((tmp, cnt + 1))

    return "Impossible"


t = int(input())

prime = [1] * 10000
checkPrime()
for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a, b))
