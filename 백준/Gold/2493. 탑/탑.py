import sys

input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

# 스택에 (인덱스, 높이)를 넣자
stack = []

# 결과값
ans = []

for i in range(N):
    while stack: # 스택이 있다면
        if stack[-1][1] >= data[i]: # 스택의 top값이 현재 값보다 크면
            ans.append(stack[-1][0] + 1) # 탑의 번호 삽입
            break
        else: # 스택의 top값이 현재 값보다 작으면
            stack.pop() # 스택에서 빼기

    if not stack: # 스택이 없다면
        ans.append(0) # 비교할 값이 없어서 0 삽입

    stack.append((i, data[i])) # 현재값과 인덱스 삽입

print(*ans)