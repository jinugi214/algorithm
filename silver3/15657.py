from itertools import product

n, m = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

result = []

def Dfs(depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return

    for i in range(n):
        if depth == 0 or result[depth - 1] <= data[i]:
            result.append(data[i])
            Dfs(depth + 1)
            result.pop()

Dfs(0)

'''
비내림차순이란, 각각의 원소가 바로 앞에 있는 원소보다 크거나 같을 경우를 말한다.
만약 그러한 수열이 여러개라면 사전순으로 앞서는 것을 출력한다.
'''