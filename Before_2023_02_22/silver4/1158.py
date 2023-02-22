import sys

input = sys.stdin.readline

n, k = map(int, input().split())

data = [i for i in range(1, n + 1)] # 1번부터 N번까지 사람들 

answer = [] # 제거된 인덱스를 넣는 리스트

# 인덱스는 0부터 시작하기에 -1을 해준다.
num = k - 1

for i in range(n):
    if len(data) > num:
        answer.append(data.pop(num))
        num += k - 1
        
    # num이 리스트의 길이보다 크거나 같으면 그 값을 리스트의 길이로 나눈 나머지 값으로 설정
    elif len(data) <= num:
        num = num % len(data)
        answer.append(data.pop(num))
        num += k - 1
# sep =''를 추가해줘야지 <,>와 숫자 사이에 공백이 생기지 않는다.
print("<", ', '.join(str(i) for i in answer), ">", sep = '')

