import sys

input = sys.stdin.readline

n = int(input())

list = list(map(int, input().split()))

answer = [-1] * n

stack = []

for i in range(n):
    # 스택 마지막 인덱스의 값보다 큰 값이 있을 경우
    while stack and (list[stack[-1]] < list[i]):
        answer[stack[-1]] = list[i]
        stack.pop()
    stack.append(i)

print(*answer)
