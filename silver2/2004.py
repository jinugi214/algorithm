import sys

input = sys.stdin.readline

n, m = map(int, input().split())

def count_num(a, b):
    count = 0
    while a:
        a = a // b
        count += a
    return count

count_five = count_num(n, 5) - count_num(m, 5) - count_num(n - m , 5)
count_two = count_num(n, 2) - count_num(m, 2) - count_num(n - m, 2)

result = min(count_five, count_two)

print(result)

# 조합 nCr 서로 다른 n개 중, r개를 선택하는 경우의 수 (순서 중요x)

# 공식 n! / ((n-r)! * r !)

# 하지만 이 공식으로 하면 시간초과 발생

# 끝자리 0은 구하는 것은 2와 5곱인 10으로 이루어진 것 ex) xxx00이면 2 * 5가 2번 된 것

# 2와 5의 짝이 맞아야 10이 되므로 2의 개수와 5의 개수 중 더 작은 개수가 10의 개수이다.

# 식이 나누기 이므로 약분을 하면 갯수를 빼주면 되기 때문에
# a의 지수 = n!의 a의 지수 - (n-r)!의 a의 지수 - r!의 a의 지수
