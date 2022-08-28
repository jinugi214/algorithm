import sys

input = sys.stdin.readline

data = list(input().rstrip())

answer = 0
stick = []

for i in range(len(data)):
    if data[i] == '(':
        stick.append('(')

    # (가 아닌 )인 경우
    else:
        # ()일 경우 (를 pop 해주고 스택에 들어있는 ( 수 만큼 더해준다.
        if data[i-1] == '(':
            stick.pop()
            answer += len(stick)
        
        # )) 일 경우
        else:
            stick.pop()
            answer += 1

print(answer)