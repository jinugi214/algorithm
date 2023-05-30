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
    elif x <= burger[n - 1] + 1:  # x값이 n버거의 절반 값보다 낮으면
        return eat(n - 1, x - 1)
    elif x == 1 + burger[n - 1] + 1:  # x값이 n버거의 절반 값이면
        return patty[n - 1] + 1
    elif x <= 1+ burger[n - 1] + 1 + burger[n - 1]: # x값이 n버거보다 클 때
        return patty[n - 1] + 1 + eat(n - 1, (x - (burger[n - 1] + 2)))
    else: # 끝까지 다 먹은 경우
        return patty[n]


print(eat(N, X))
