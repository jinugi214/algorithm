import sys

input = sys.stdin.readline

N, M = map(int, input().split())

l = list(map(int, input().split()))

l.sort()

d = []


def dfs(start):
    if len(d) == M:
        print(' '.join(map(str, d)))
        return
    
    for i in range(start, N):
        d.append(l[i])
        dfs(i+1)
        d.pop()

dfs(0)
