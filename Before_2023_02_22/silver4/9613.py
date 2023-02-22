import sys

input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

t = int(input())

for _ in range(t):
    # GCD 최대공약수
    # 첫번째 값은 넣는 값 개수
    nums = list(map(int, input().split()))

    answer = 0

    for i in range(1, nums[0] + 1):
        for j in range(i + 1, nums[0] + 1):
            answer += gcd(nums[i], nums[j])

    print(answer)