import sys
from collections import deque

input = sys.stdin.readline

while True:
    data = list(input().rstrip())
    if len(data) == 1 and data[0] == '.':
        break

    q = deque()

    for i in data:
        if i == '(' or i == '[':
            q.append(i)
        elif i == ')':
            if q and q[-1] == '(':
                q.pop()
            else:
                print('no')
                break
        elif i == ']':
            if q and q[-1] == '[':
                q.pop()
            else:
                print('no')
                break
    else:
        if len(q) > 0:
            print('no')
        elif len(q) == 0:
            print('yes')