import sys

input = sys.stdin.readline

N, M = map(int, input().split())

d = []

def dfs(start):
    if len(d) == M:
        print(' '.join(map(str, d)))
        return
    
    for i in range(start, N + 1):
        d.append(i)
        dfs(i)
        d.pop()
        
dfs(1)