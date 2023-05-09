# 백준 19942
import sys

input = sys.stdin.readline

N = int(input())

mp, mf, ms, mv = map(int, input().split())


def dfs(k):
    global rlt, rlt_lst
    p, f, s, v, c = 0, 0, 0, 0, 0
    for i in comb:
        p += data[i][0]
        f += data[i][1]
        s += data[i][2]
        v += data[i][3]
        c += data[i][4]

    # 최소 영양성분을 충족하면
    if p >= mp and f >= mf and s >= ms and v >= mv:
        if c < rlt:  # 최소비용이면
            rlt = c
            rlt_lst = [i for i in comb]  # 식재료도 옮기기
        if c == rlt and rlt_lst[0] > comb[0]:  # 같은 비용이면 사전순으로 빠른 것 출력
            rlt_lst = [i for i in comb]

    # 재료를 1~ N개를 선택하는 조합
    for i in range(k, N + 1):
        if i not in comb:
            comb.append(i)
            dfs(i + 1)
            comb.pop()


data = [[0] * 5] + [list(map(int, input().split())) for _ in range(N)]

rlt = 1e9
rlt_lst = []
comb = []
dfs(1)

if rlt == 1e9:
    print(-1)
else:
    print(rlt)

if rlt_lst:
    print(*rlt_lst)
