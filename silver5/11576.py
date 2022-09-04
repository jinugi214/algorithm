import sys

input = sys.stdin.readline

# a진법을 b진법으로 나타내기
a, b = map(int, input().split())

# a진법으로 나타낸 숫자의 자리수의 개수
m = int(input())

# a진법을 이루고 있는 숫자 m개가 공백을 구분으로 높은 자릿수부터
num = list(map(int, input().split()))

# a진법 -> 10진법
ten = 0
for i in range(m):
    ten = (a * ten) + num[i]

# 10진법 -> b진법
result = []
while ten != 0:
    result.append(ten % b)
    ten = ten//b

result.reverse()
print(*result)

