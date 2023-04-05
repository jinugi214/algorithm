# 회의실 배정
# dfs로 풀이시에 시간초과
# 그리디로 풀어야한다.

import sys

input = sys.stdin.readline


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data.sort(key=lambda x: (x[1], x[0])) # 회의가 빨리 끝나는 순으로 정렬하고 회의가 빨리 시작하는 순으로 정렬
prev = 0 # 이전에 끝난 시간
cnt = 0 # 회의 개수
for s, e in data:
    if s >= prev: # 끝나고 다음 회의를 시작할 수 있으면
        cnt += 1 # 회의 개수 추가
        prev = e # 끝난시간을 해당 회의의 끝난시간으로 갱신

print(cnt)