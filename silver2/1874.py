import sys
        
input = sys.stdin.readline
        
n = int(input())
stack = []
sign = []
count = 0
check = True
for i in range(n):
    num = int(input())
    # num이하 숫자까지 스택에 넣기
    while count < num:
        count += 1
        stack.append(count)
        sign.append('+')
        
        
    # num이랑 스택 맨 위 숫자가 동일하다면 제거    
    if stack[-1] == num:
        stack.pop()
        sign.append('-')
        
    # 스택 수열을 만들 수 없으면 False
    else:
        check = False
        
# 스택 수열을 만들 수 있는 지 확인
if check == False:
    print('NO')
else:
    for i in sign:
        print(i)