import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, op):
    q = deque()
    q.append((start, op))

    while q:
        num, op = q.popleft()
        used[num] = 1
        if num == B:
            return op

        # D
        new_n = (2 * num) % 10000
        if not used[new_n]:
            used[new_n] = 1
            q.append((new_n, op + 'D'))

        # S
        new_n = (num - 1) % 10000
        if not used[new_n]:
            used[new_n] = 1
            q.append((new_n, op + 'S'))

        # L
        new_n = (10 * num + (num // 1000)) % 10000
        if not used[new_n]:
            q.append((new_n, op + 'L'))
            used[new_n] = 1

        # R
        new_n = (num // 10 + (num % 10) * 1000) % 10000
        if not used[new_n]:
            q.append((new_n, op + 'R'))
            used[new_n] = 1


T = int(input())

for _ in range(T):
    # A는 레지스터의 초기값 B는 최종값
    A, B = map(int, input().split())
    used = [0] * 10000
    print(bfs(A, ''))

'''
숫자로 DSLR의 과정을 해결하면 되었는데 문자열로 바꾸어 해결할려고 했다가 시행착오를 겪었다.
Python3로 제출시 시간초과 PyPy3시 통과
'''
