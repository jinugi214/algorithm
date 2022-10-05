import sys

input = sys.stdin.readline

s = set()

m = int(input())

for i in range(m):
    tmp = input().split()
    if len(tmp) == 1:
        com = tmp[0]      
        if com == 'all':
            s = set([i for i in range(1, 21)])
        elif com == 'empty':
            s = set()     
    else:
        com, num = tmp[0], tmp[1]
        num = int(num)
        
        if com == 'add':
            s.add(num)
        elif com == 'remove':
            s.discard(num)
        elif com == 'check':
            print(1 if num in s else 0)
        elif com == 'toggle':
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        

