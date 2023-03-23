import sys
input = sys.stdin.readline
N = int(input())
max_a, max_b, max_c = map(int, input().split())
min_a, min_b, min_c = max_a, max_b, max_c
for _ in range(N-1):
    d, e, f = map(int, input().split())
    a = d + max((max_a, max_b))
    b = e + max((max_a, max_b, max_c))
    c = f + max((max_b, max_c))
    max_a, max_b, max_c = a, b, c

    a = d + min((min_a, min_b))
    b = e + min((min_a, min_b, min_c))
    c = f + min((min_b, min_c))
    min_a, min_b, min_c = a, b, c

print(max((max_a, max_b, max_c)), min((min_a, min_b, min_c)))