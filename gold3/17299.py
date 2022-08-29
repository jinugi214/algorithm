import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

data = list(input().split())

num = Counter(data)

answer = [-1] * n

stack = []

# 오른쪽에 있으면서 수열에서 등장한 횟수가 해당 횟수보다 큰 수 중에서 가장 왼쪽에 있는 수

for i in range(n):
    # 스택의 맨 위에 존재하는 값의 중복 개수가 현재의 input값보다 작을 경우
    # 즉, 오른쪽에 첫번째 오등큰수가 나올 경우 stack 맨 위의 자리에있는 값을 data[i]로 변경한다.
    while stack and (num[data[stack[-1]]] < num[data[i]]):
        answer[stack.pop()] = data[i]
    stack.append(i)

print(*answer)
