N, M = map(int, input().split())

data = [i for i in range(1,N+1)]

for i in range(M):
    i, j = map(int, input().split())
    rdata = data[i-1:j]
    rdata.reverse()
    data[i-1:j] = rdata

for i in range(N):
    print(data[i], end = ' ')