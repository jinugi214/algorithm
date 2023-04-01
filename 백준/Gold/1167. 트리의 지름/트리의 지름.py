import sys

input = sys.stdin.readline

def dfs(s, val):
    global node_num, distance
    used[s] = 1

    for line in tree[s]:
        n, v = line
        if tree[n] and not used[n]:
            dfs(n, val + v)
    else:
        if val > distance:
            node_num = s
            distance = val
V = int(input())

tree = [[] for _ in range(V + 1)]

for _ in range(V):
    data = list(map(int, input().split()))

    for i in range(1, len(data) - 1, 2):
        tree[data[0]].append((data[i], data[i + 1]))

# 1에서 가장 먼 루트 찾고 그 루트에서 dfs로 값 비교하기
distance = 0
node_num = 0
used = [0] * (V + 1)
dfs(1, 0)

used = [0] * (V + 1)
distance = 0
dfs(node_num, 0)
print(distance)