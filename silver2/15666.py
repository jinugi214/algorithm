n, m = map(int, input().split())

data = sorted(list(set(map(int, input().split()))))

result = []

def dfs(depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(len(data)):
        if depth == 0 or result[-1] <= data[i]:
            result.append(data[i])
            dfs(depth + 1)
            result.pop()
        
dfs(0)