import sys

input = sys.stdin.readline

n = int(input())

Postfix = input().rstrip()

num_list = []

for _ in range(n):
    num_list.append(int(input()))

stack = []

for i in Postfix:
    if i.isalpha():
        stack.append(num_list[ord(i)-ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()
        
        if i == '+':
            stack.append(a + b)
        elif i == '-':
            stack.append(a - b)
        elif i == '*':
            stack.append(a * b)
        elif i == '/':
            stack.append(a / b)
        
print('%.2f' %stack[0])