data = input()

for i in range(0, len(data)):
    if data[i] != data[(len(data)-1)-i]:
        print(0)
        break
else:
    print(1)