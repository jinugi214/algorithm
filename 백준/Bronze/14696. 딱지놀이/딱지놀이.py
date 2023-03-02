import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):

    data1 = list(map(int, input().split()))
    # 별, 동그라미, 네모, 세모

    data2 = list(map(int, input().split()))

    M = max(data1[0], data2[0])

    data = [[0] * 2 for _ in range(M+1)]

    for i in data1[1:]:
        data[i][0] += 1

    for i in data2[1:]:
        data[i][1] += 1

    for i in range(M, 0, -1):
        if data[i][0] == data[i][1]:
            if i == 1:
                print('D')
                break
            continue
        elif data[i][0] > data[i][1]:
            print('A')
            break
        elif data[i][0] < data[i][1]:
            print('B')
            break

    # A가 승자라면 A, B가 승자라면 B, 무승부라면 D이다.
