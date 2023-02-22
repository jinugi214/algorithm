n, m = map(int, input().split())

data = sorted(list(map(int, input().split())))

visited = [False] * n

temp = []

def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    previous = 0
    for i in range(start, n):
        if not visited[i] and previous != data[i]:
            visited[i] = True
            temp.append(data[i])
            previous = data[i]
            dfs(i + 1)
            visited[i] = False
            temp.pop()

dfs(0)
