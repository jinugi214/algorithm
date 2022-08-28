import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

list = list(map(int, input().split()))

answer = [-1] * n

stack = []

for i in range(n):
    while stack and (list[stack[-1]] < list[i]):
        answer[stack[-1]] = list[i]
        stack.pop()
    stack.append(i)

print(*answer)
