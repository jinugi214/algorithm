# A -> B 최소값

def dfs(val, cnt):
    check.add((val, cnt))
    global ans

    if val == B:
        if cnt < ans:
            ans = cnt
        return

    if val > B:
        return

    if (val * 2, cnt+1) not in check:
        dfs(val * 2, cnt+1)

    if (int(str(val) + '1'), cnt + 1) not in check:
        dfs(int(str(val) + '1'), cnt + 1)


A, B = map(int, input().split())

check = set()

ans = 1e9

dfs(A, 1)

if ans == 1e9:
    ans = -1

print(ans)