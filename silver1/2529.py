K = int(input())
sign_list = list(input().split())

arr = [i for i in range(10)]


def check(a, b, sign):  # 숫자가 다 다르기 때문에 =는 필요 없다.
    if sign == '>':
        if a > b:
            return True
        else:
            return False
    elif sign == '<':
        if a < b:
            return True
        else:
            return False
    else:
        print('이상한 부호가 들어왔습니다.')


def permutation(arr, r):
    used = [0 for _ in range(len(arr))]
    ans = []

    def generate(chosen, used):
        if len(chosen) > 1:
            idx = len(chosen) - 2
            if not check(chosen[-2], chosen[-1], sign_list[idx]):
                return

        if len(chosen) == r:
            ans.append(''.join(map(str, chosen)))
            return

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)
    return ans


ans = permutation(arr, K + 1)

print(max(ans))
print(min(ans))
