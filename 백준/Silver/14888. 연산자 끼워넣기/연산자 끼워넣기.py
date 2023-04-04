from itertools import permutations
import sys

input = sys.stdin.readline

def dfs(p, m, s, d, val, cnt):
    global max_v, min_v
    if cnt == N:
        max_v = max(max_v, val)
        min_v = min(min_v, val)
    if p:
        dfs(p-1, m, s, d, val + data[cnt], cnt+1)
    if m:
        dfs(p, m-1, s, d, val - data[cnt], cnt + 1)
    if s:
        dfs(p, m, s-1, d, val * data[cnt], cnt + 1)
    if d:
        dfs(p, m, s, d-1, int(val / data[cnt]), cnt + 1)

N = int(input())
data = list(map(int, input().split()))
p, m, s, d = map(int, input().split())

max_v = -1e9
min_v = 1e9
dfs(p, m, s, d, data[0], 1)
print(max_v)
print(min_v)