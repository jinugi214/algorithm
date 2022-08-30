import sys

input = sys.stdin.readline

while True:
    temp = input().rstrip('\n')
    # rstrip에 \n을 따로 지정해주지 않으면 오른편에 공백도 다 제거된다.
    if not temp:
        break
    
    lower, upper, num, blank = 0, 0, 0, 0
    for x in temp:
        if x.islower():
            lower += 1
        elif x.isupper():
            upper += 1
        elif x.isdigit():
            num += 1
        elif x.isspace():
            blank += 1
            
    print(lower, upper, num, blank)
