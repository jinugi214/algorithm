import sys

input = sys.stdin.readline

# 듣도 못한 사람 N, 보도 못한 사람 M
N, M = map(int, input().split())

nl = []
ns = []
for _ in range(N):
    nl.append(input().rstrip())
for _ in range(M):
    ns.append(input().rstrip())

dif = set(nl) - set(ns)

rlt = list(set(nl) - dif)

rlt.sort()
print(len(rlt))
for x in rlt:
    print(x)