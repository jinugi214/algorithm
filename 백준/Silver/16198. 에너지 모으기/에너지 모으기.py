import sys

input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

def dfs(x):
    global energy

    if len(data) == 2:
        energy = max(energy, x)
        return

    for i in range(1, len(data)-1):
        max_val = data[i-1] * data[i+1]

        del_val = data.pop(i)
        dfs(x + max_val)
        data.insert(i, del_val)

energy = 0

dfs(0)

print(energy)