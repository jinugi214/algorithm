def recursion(s, l, r):
    global cnt
    cnt += 1 # 재귀할 때마다 횟수 추가
    if l >= r: # 팰린드롬이면
        return 1
    elif s[l] != s[r]: # 팰린드롬이 아니면
        return 0
    else:
        return recursion(s, l + 1, r - 1) # 재귀로 계속해서 확인


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)


T = int(input())

for _ in range(T):
    S = input()
    cnt = 0
    print(isPalindrome(S), cnt)
