# 에라토스테네스의 체 활용
import sys

input = sys.stdin.readline

prime = [True for i in range(1000001)]

for i in range(2, 1001): # 제곱근까지 확인
    if prime[i]: # 소수이면
        for j in range(i*2, 1000001, i): # 배수들 다 소수X 만들어주기
            prime[j] = False


while True:
    val = int(input())

    if val == 0:
        break

    for i in range(3, val-1, 2):
        if prime[i] and prime[val-i]: # b-a 가장 큰 것
            print(val, '=', i, '+', val-i)
            break
    else:
        print("Goldbach's conjecture is wroing")
