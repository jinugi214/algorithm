N, X = map(int, input().split())

burger = [1] * 51
patty = [1] * 51

for i in range(1, N + 1):
    burger[i] = 1 + burger[i - 1] + 1 + burger[i - 1] + 1
    patty[i] = patty[i - 1] + 1 + patty[i - 1]

def eat(n, x):
    if n == 0:
        return x
    if x == 1:
        return 0
    elif x <= burger[n - 1] + 1:  # 버거의 절반보다 덜 먹었으면
        return eat(n - 1, x - 1)
    elif x == 1 + burger[n - 1] + 1:  # 버거의 절반만 먹었을 경우
        return patty[n - 1] + 1
    elif x <= 1+ burger[n - 1] + 1 + burger[n - 1]: # 버거의 절반보다 더 먹었지만 다 안 먹은 경우
        return patty[n - 1] + 1 + eat(n - 1, (x - (burger[n - 1] + 2)))
    else: # 버거를 끝까지 다 먹은 경우
        return patty[n]


print(eat(N, X))
