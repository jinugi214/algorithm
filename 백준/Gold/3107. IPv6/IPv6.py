data = list(input().split(':'))

if data.count('') == 2:
    data.remove('')
lmt = 8 - len(data) + 1
rlt = []
flag = 0
for x in data:
    if x == '':
        for _ in range(lmt):
            rlt.append('0000')
            rlt.append(':')
    else:
        while len(x) != 4:
            x = '0' + x
        rlt.append(x)
        rlt.append(':')
rlt.pop()
for x in rlt:
    print(x, end='')