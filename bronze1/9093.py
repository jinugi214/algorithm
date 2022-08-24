t = int(input())

for i in range(t):
    string = input()
    string += " " # 마지막 단어도 stack에서 꺼낼 수 있게 구현
    stack = []
    for j in string: # 단어 한개씩 지정
        if j != " ": # 공백이 아닐 경우 stack리스트에 넣기
            stack.append(j)
        else: # 공백일 경우 
            while stack: # 공백전에 리스트안에 들어있는 단어를 pop으로 한글자씩 꺼내기
                print(stack.pop(), end= "")
            print(" ", end= "")  
''' 
# 2번째 방법

t = int(input())

for i in range(t):
    string = list(input().split())
    for j in string:
        print(j[::-1], end= ' ')
'''  