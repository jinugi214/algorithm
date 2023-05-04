N = int(input())
factors = list(map(int, input().split()))

print(min(factors) * max(factors))