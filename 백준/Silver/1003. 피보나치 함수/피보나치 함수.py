# 피보나치 함수
def fib(N):
    zeros = [1, 0, 1] # 0이 출력되는 횟수 리스트
    ones = [0, 1, 1] # 1이 출력되는 횟수 리스트
    if N >= 3:
        for i in range(2, N):
            zeros.append(zeros[i - 1] + zeros[i]) # 피보나치 수열을 이용
            ones.append(ones[i - 1] + ones[i]) # 피보나치 수열을 이용
    print(f"{zeros[N]} {ones[N]}") # 해당 N값에서 0과 1 출력되는 횟수


T = int(input())
for _ in range(T):
    N = int(input())
    fib(N)
