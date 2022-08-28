import sys

input = sys.stdin.readline

s = list(input().rstrip())

i = 0
start = 0

while i<len(s):
    if s[i] == "<": # 열린 괄호를 만날 경우
        while s[i] != '>': # 닫힌 괄호를 만날 때 까지
            i += 1
        i += 1  # 닫힌 괄호 만난 후에 인덱스 증가
    elif s[i].isalnum(): # 숫자나 알파벳을 만나면
        start = i
        # 현재 문자 위치와 숫자 알파벳인지 확인
        while i < len(s) and s[i].isalnum():
            i += 1
        temp = s[start:i] #
        temp.reverse()
        s[start:i] = temp
    else:
        i += 1 # 괄호, 알파벳, 숫자 아닌 공백인 경우
        
print("".join(s))