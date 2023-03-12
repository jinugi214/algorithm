# 중복이 가능한 조합

'''
# 조합 직접 구현시 (시간초과)
def combination(lst, r):
    rlt = set()

    def generate(chosen):
        if len(chosen) == r:
            rlt.add(sum(chosen))
            return

        for i in range(len(lst)):
            chosen.append(lst[i])
            generate(chosen)
            chosen.pop()

    generate([])
    return len(rlt)
'''

'''
# itertools 라이브러리로 중복조합 구현

from itertools import combinations_with_replacement

N = int(input())  # 문자의 개수 입력

lst = [1, 5, 10, 50]

data = list(combinations_with_replacement(lst, N))

rlt = set()
for i in data:
    rlt.add(sum(i))

# 만들 수있는 수의 개수를 찾기
print(len(rlt))
'''

# 반복문을 사용해 구현 (lst안의 숫자가 많아지면 불가능한 방법)
N = int(input())  # 문자의 개수 입력

lst = [1, 5, 10, 50]

rlt = set() # 중복 방지를 위해 set으로 선언

for i in range(N+1): # 1 선택 개수
    for j in range(N+1 - i): # 5 선택 개수
        for k in range(N + 1 - i - j): # 10 선택개수
            t = N-i-j-k # 50 선택개수
            n = lst[0] * i + lst[1] * j + lst[2] * k + lst[3] * t
            rlt.add(n) # set에 추가
# 만들 수있는 수의 개수를 찾기

print(len(rlt))# set안의 수의 개수들 출력
