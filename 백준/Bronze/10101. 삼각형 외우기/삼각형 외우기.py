lst = [int(input()) for _ in range(3)]

if sum(lst) == 180:
    for i in range(2):
        if lst.count(lst[i]) == 2:
            print('Isosceles')
            break
        elif lst.count(lst[i]) == 3:
            print('Equilateral')
            break
    else:
        print('Scalene')

else:
    print('Error')

