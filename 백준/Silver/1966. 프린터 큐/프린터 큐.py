from collections import deque
import sys

input = sys.stdin.readline

# 중요도가 높은 것부터 먼저 큐에서 빠져나가도록 한다.

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    # 문서의 개수 N, 몇 번째로 인쇄되었는지 궁금한 문서 M
    important = deque(list(map(int, input().split())))
    # N개 문서의 중요도들 important
    max_i = max(important)  # 중요도 최댓값
    idx = deque([i for i in range(0, N)])

    cnt = 0  # 횟수 세기
    while True:
        i = important.popleft()
        d = idx.popleft()
        if i == max_i:
            max_i -= 1  # 중요도 최댓값이 빠졌기 때문에 -1
            cnt += 1  # 인쇄 횟수
            if important:
                max_i = max(important)
            if d == M:
                print(cnt)
                break
        else:
            important.append(i)
            idx.append(d)
