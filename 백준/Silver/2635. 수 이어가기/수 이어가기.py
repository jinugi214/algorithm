N = int(input())

max_v = 0
max_lst = []
for i in range(1, N+1):
    data = [N, i]
    idx = 0

    while True:
        nx = data[idx] - data[idx + 1]
        if nx < 0:
            if max_v < len(data):
                max_v = len(data)
                max_lst = data
            break
        data.append(nx)
        idx += 1

print(max_v)
print(*max_lst, sep=' ')