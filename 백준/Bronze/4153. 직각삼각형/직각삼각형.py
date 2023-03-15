# 피타고라스의 정리 활용하기

while True:
    data = list(map(int, input().split()))

    if sum(data) == 0:
        break

    data.sort()

    ausar = data[0]
    auset = data[1]
    heru = data[2]

    if ausar ** 2 + auset ** 2 == heru ** 2:
        print('right')
    else:
        print('wrong')
