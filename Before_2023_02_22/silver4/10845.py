import sys

input = sys.stdin.readline

n = int(input())

data = []

for _ in range(n):
    command = list(input().split())
    
    if command[0] == 'push':
        data.append(command[1])
    
    elif command[0] == 'front':
        if data:
            print(data[0])
        else:
            print(-1)
    
    elif command[0] == 'back':
        if data:
            print(data[-1])
        else:
            print(-1)
    
    elif command[0] == 'size':
        print(len(data))
    
    elif command[0] == 'empty':
        if data:
            print(0)
        else:
            print(1)
    
    elif command[0] == 'pop':
        if data:
            print(data.pop(0))
        else:
            print(-1)