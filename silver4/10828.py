import sys

n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    command = sys.stdin.readline().split()
        
    if command[0] == 'push':
        stack.append(command[1])   
    if command[0] == 'pop':
        if stack:
                print(stack.pop())
        else:
            print(-1)   
    if command[0] == 'size':
        print(len(stack))   
    if command[0] == 'empty':
        if not stack:
            print(1)
        elif stack:
            print(0)
    if command[0] == 'top':
        if stack:
            print(stack[-1])
        elif not stack:
            print(-1)  
