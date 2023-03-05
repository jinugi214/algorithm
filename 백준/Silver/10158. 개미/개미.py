from collections import deque

w, h = map(int, input().split())  # 격자 공간
p, q = map(int, input().split())  # 출발 위치
t = int(input())  # t시간 후 위치 구하기

x = (p + t) // w # 증가, 감소부분인지 확인
y = (q + t) // h
# x축을 기준으로 홀수일 떄는 왼쪽으로 짝수일 때는 오른쪽으로 이동한다.


if x % 2 == 0: # 증가 부분일 경우
    ans_x = (p + t) % w
else: # 감소 부분일 경우
    ans_x = w - (p + t) % w

if y % 2 == 0:
    ans_y = (q + t) % h
else:
    ans_y = h - (q + t) % h

print(ans_x, ans_y)