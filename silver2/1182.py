def backtracking(idx, sum_value):
    global cnt

    if idx >= n:
        return

    sum_value += data[idx]

    if sum_value == s:
        cnt += 1

    backtracking(idx+1, sum_value)

    backtracking(idx+1, sum_value - data[idx])


n, s = map(int, input().split())

data = list(map(int, input().split()))

cnt = 0

backtracking(0, 0)

print(cnt)