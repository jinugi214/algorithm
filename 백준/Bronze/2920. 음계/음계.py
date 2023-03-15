data = list(map(int, input().split()))

a_cnt = 0
d_cnt = 0
for i in range(8):
    if data[i] == i+1:
        a_cnt += 1
    elif data[i] == 8-i:
        d_cnt += 1

if a_cnt == 8:
    print('ascending')
elif d_cnt == 8:
    print('descending')
else:
    print('mixed')