from collections import deque
from itertools import combinations
from copy import deepcopy

A, B, C = map(int, input().split())

check = set()

def bfs():

    q = deque()
    q.append((A, B, C))

    while q:
        tmp = q.popleft()
        if len(set(tmp)) == 1:
            return 1
        lst = list(combinations(tmp, 2))
        for x in lst:
            if x[0] != x[1]:
                mx, mn = max(x), min(x)
                tmp_lst = list(deepcopy(tmp))
                tmp_lst.remove(mx)
                tmp_lst.remove(mn)
                if (mn + mn, mx-mn, tmp_lst[0]) not in check:
                    q.append((mn + mn, mx-mn, tmp_lst[0]))
                    check.add((mn + mn, mx-mn, tmp_lst[0]))
    return 0

print(bfs())