A, B = input().split()  # A, B 입력

# 조건
# A에 포함된 숫자의 순서를 섞어서 새로운 수 C
# 가능한 C 중에서 B보다 작으면서, 가장 큰 값

lst = list(A)


def permutation(lst, r):
    lst.sort()
    used = [0 for _ in range(len(lst))]
    max_val = -1

    def generate(chosen, used):
        nonlocal max_val
        if len(chosen) == r and chosen[0] != '0': # 0으로 시작하면 안된다.
            cur_val = int(''.join(chosen))
            if cur_val < int(B):
                max_val = max(max_val, cur_val)
            return

        for i in range(len(lst)):
            if not used[i]:
                chosen.append(lst[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)
    return max_val


print(permutation(lst, len(lst)))
