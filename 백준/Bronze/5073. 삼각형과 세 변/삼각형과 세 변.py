while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    lst = [a, b, c]
    if len(set(lst)) == 1:
        print('Equilateral')
    else:
        lst.sort()
        if lst[2] >= lst[0] + lst[1]:
            print('Invalid')
        else:
            if len(set(lst)) == 2:
                print('Isosceles')
            elif len(set(lst)) == 3:
                print('Scalene')
