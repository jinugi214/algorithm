t = int(input())

for i in range(t):
    stack = []
    data = input()
    for j in data:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: # 스택에 괄호가 없을 경우 NO
                print("NO")
                break
    else: # break로 끊기지 않았을 때 실행
        if not stack: # break 문으로 안 끊기고 스택이 비어있다면 괄호가 맞는 것
            print("YES")
        else: # break 안 걸렸더라도 스택에 괄호가 들어있으면 NO
            print("NO")