import sys

input = sys.stdin.readline

# N까지 중복없이 M개를 고른 수열
N, M = map(int, input().split())

d = []

# 오름차순 출력
def dfs(start):
    if len(d) == M: # 탈출
        print(' '.join(map(str, d)))
        return
    
    for i in range(start, N+1):
        if i not in d:
            d.append(i)
            dfs(i+1)
            d.pop()

dfs(1)