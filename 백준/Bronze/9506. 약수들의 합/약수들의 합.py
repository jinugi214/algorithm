while True:
    n = int(input())
    if n == -1:
        break

    lst = []
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)
    if sum(lst) == n:
        n = str(n)
        print(n + ' =', end='')
        for j in range(len(lst) -1 ):
            val = str(lst[j])
            print(' ' + val + ' +', end='')
        print(' ' + str(lst[-1]))
    else:
        n = str(n)
        print(n + ' is NOT perfect.')
