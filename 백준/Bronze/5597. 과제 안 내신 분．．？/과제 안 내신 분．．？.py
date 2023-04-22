stu = [0] * 31

for i in range(28):
    n = int(input())
    stu[n] = 1

for i in range(1, 31):
    if stu[i] == 0:
        print(i)