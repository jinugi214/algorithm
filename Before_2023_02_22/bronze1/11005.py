import sys
import string

input = sys.stdin.readline

tmp = string.digits + string.ascii_uppercase

n, b = map(int, input().split())

answer = str()

while n != 0:
    # n 에서 b를 나눈 값의 나머지인 값인 순서를 answer에 담는다.
    # 나머지가 4이면 tmp에서 인덱스 4인 3을 반환 
    answer += tmp[n % b]
    n = n // b

# 마지막으로 구한 값을 뒤집어 줘야한다. 
print(answer[::-1]) 

'''
362를 10진수 변환

10진수의 경우 362를 10으로 나누면 몫은 36 나머지는 2이다.
여기서 2는 10진수에서 2번째 숫자를 의미한다.

362 -> 몫 36 나머지 2 -> 몫 3 나머지 6 -> 몫 0 나머지 3
나머지들끼리 모두 더해주면 결과는 263 
맨 끝자리에 대응될 값부터 구했기 때문에 결과를 뒤집어야 진법변환이 완려된다.
값은 362

'''