import sys

input = sys.stdin.readline

N, M = map(int, input().split())

site = dict()

for _ in range(N):
    url, pwd = input().split()
    site[url] = pwd

for _ in range(M):
    furl = input().rstrip()
    print(site[furl])