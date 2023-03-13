import sys
from collections import deque

input = sys.stdin.readline

T = int(input())  # 테스트 케이스 개수

for _ in range(1, T + 1):

    p = list(input())  # 수행할 함수

    n = int(input())  # 배열에 들어있는 수의 개수

    # R은 배열에 있는 수의 순서를 뒤집는 함수이고,
    # D는 첫 번째 수를 버리는 함수이다.
    # 배열이 비어있는데 D를 사용한 경우에는 에러가 발생

    data = deque(input()[1:-2].split(',')) # 양쪽 [] 제외하고 ,로 별로 나눠서 받기

    if n == 0:
        data = deque([])
    
    rev = 0 # 뒤집기 횟수
    error = False # 플래그 변수
    for i in p:
        if i == 'R': # 뒤집기 함수
            rev += 1 # 뒤집기 횟수 추가
        elif i == 'D': # 버리는 함수
            if not len(data): # queue안에 아무것도 없으면
                error = True # 에러발생
                print('error')
                break
            else:
                if rev % 2 == 0: # 뒤집기 두번은 원래상태이므로 앞에서 빼야한다.
                    data.popleft()
                else: # 뒤집은 상태이면 뒤에서 빼야한다.
                    data.pop()

    if not error: # 에러가 아니면
        if rev % 2 == 0: # 뒤집은 상태가 아니면
            print('[' + ','.join(data) + ']')
        else: # 뒤집은 상태이면
            data.reverse()
            print('[' + ','.join(data) + ']')