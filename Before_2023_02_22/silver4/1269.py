# 대칭 차집합

A, B = map(int, input().split())
A_lst = list(map(int, input().split()))
B_lst = list(map(int, input().split()))

ans1 = set(A_lst) - set(B_lst)
ans2 = set(B_lst) - set(A_lst)

print(len(ans1) + len(ans2))