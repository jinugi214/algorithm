N = int(input())

for i in range(N):
    print(' ' * ((N-1) - i) + ('*' * ((2 * i) + 1)))

for i in range(N-2, -1, -1):
    print(' ' * ((N-1)- i) + ('*' * ((2 * i) + 1)))