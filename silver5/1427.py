n = list(map(int, str(input())))

n.sort(reverse=True)

n = map(str, n)

print(''.join(n))