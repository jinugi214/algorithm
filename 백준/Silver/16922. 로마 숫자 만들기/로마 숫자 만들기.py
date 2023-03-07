from itertools import combinations_with_replacement

N = int(input())  # 문자의 개수 입력

lst = [1, 5, 10, 50]

data = list(combinations_with_replacement(lst, N))

rlt = set()
for i in data:
    rlt.add(sum(i))

# 만들 수있는 수의 개수를 찾기
print(len(rlt))