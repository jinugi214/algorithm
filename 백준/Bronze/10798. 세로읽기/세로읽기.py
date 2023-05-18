data = [list(input()) for _ in range(5)]

max_len = 0

for i in range(5):
    max_len = max(max_len, len(data[i]))

for i in range(max_len):
    for j in range(5):
        try:
            print(data[j][i], end='')
        except(IndexError):
            continue
