N = int(input())

switch = [0] + list(map(int, input().split()))

S = int(input())


def change(n):
    if switch[n] == 0:
        switch[n] = 1
    elif switch[n] == 1:
        switch[n] = 0


for _ in range(S):
    type, num = map(int, input().split())

    if type == 1:
        for i in range(1, len(switch)):
            if i % num == 0:
                change(i)

    elif type == 2:
        change(num)

        for i in range(1, len(switch)):
            if 1 <= num - i < num < num + i < len(switch):
                if switch[num - i] == switch[num + i]:
                    change(num - i)
                    change(num + i)

                elif switch[num - i] != switch[num + i]:
                    break
            else:
                break

for i in range(1, len(switch)):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()
