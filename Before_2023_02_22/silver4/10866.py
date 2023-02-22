import sys
from collections import deque

n = int(input())

input = sys.stdin.readline

data = deque()

for _ in range(n):
    command = list(input().split())
    if command[0] == 'push_front':
        data.appendleft(command[1])
        
    elif command[0] == 'push_back':
        data.append(command[1])

    elif command[0] == 'pop_front':
        if data:
            print(data.popleft())
        else:
            print(-1)

    elif command[0] == 'pop_back':
        if data:
            print(data.pop())
        else:
            print(-1)

    elif command[0] == 'size':
            print(len(data))

    elif command[0] == 'empty':
        if data:
            print(0)
        else:
            print(1)

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