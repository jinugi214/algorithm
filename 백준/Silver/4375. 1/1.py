while True:
    try:
        n = int(input())
    except(Exception):
        break
    val = '1'
    while True:
        if int(val) % n == 0:
            print(len(val))
            break
        else:
            val += '1'
