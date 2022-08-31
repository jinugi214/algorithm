import sys

input = sys.stdin.readline

num1, num2 = map(int, input().split())

#최대공약수 
def gcd(num1 , num2):
    while num2 > 0:
        num1, num2 = num2, num1 % num2
    return num1

#최소공배수
def lcm(num1, num2):
    return num1 * num2 // gcd(num1, num2)

print(gcd(num1, num2))
print(lcm(num1, num2))