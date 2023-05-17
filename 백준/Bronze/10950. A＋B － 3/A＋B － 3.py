N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    print(lst[i][0] + lst[i][1])