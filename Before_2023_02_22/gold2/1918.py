import sys
input = sys.stdin.readline

infix = input().rstrip()

stack = []
result = ''

for i in infix:
    if i.isalpha():
        result += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                result += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-': 
            # 우선 순위가 떨어지는 부호이기 때문에 stack에 넣기 전에 미리 stack에 있는 부호를 빼서 result에 넣어준다.
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(i)
        elif i == ')':
            # ( 가 나오기전 까지 stack에 값을 빼서 result에 더해준다.
            while stack and stack[-1] != '(':
                result += stack.pop()
            # ( 를 없애준다.
            stack.pop()

# 스택 안에 남아있는 값들 pop
while stack:
    result += stack.pop()
print(result)
