while True:
    val = input()

    if val == '0':
        break

    lmt = len(val) // 2
    for i in range(lmt):
        if val[i] == val[-(i + 1)]:
            pass
        else:
            print('no')
            break
    else:
        print('yes')
