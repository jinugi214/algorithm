N = int(input())

data = list(map(int, input().split()))

num = int(input())

cnt = 0
for i in data:
    if i == num:
        cnt+=1

print(cnt)