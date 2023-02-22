import sys

input = sys.stdin.readline


# 답이 k이면 (k-x)%m = 0 and (k-y)%n = 0

def check(M, N, x, y):
    while x <= M * N:
        if (x - y) % N == 0: # x = k 가 된다면 답은 x
            return x
        x += M # k는 x에 계속 m을 더한 값 중 하나
    return -1

T = int(input())

for _ in range(T):
    cnt = 0 # 횟수
    M, N, x, y = list(map(int, input().split())) #입력
    print(check(M, N, x, y))


