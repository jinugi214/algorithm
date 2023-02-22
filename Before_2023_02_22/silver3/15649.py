import sys
from itertools import permutations

input = sys.stdin.readline

# n개까지 중복없이 m개를 고른 수열
n, m = map(int, input().split())

data = []

for i in range(1, n + 1):
    data.append(i)

result = list(permutations(data, m))

for i in result:
    for j in i:
        print(j, end=" ")
    print()
    
''' DFS 백트래킹으로 풀 경우
n,m = list(map(int,input().split()))

s = []

def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()

'''