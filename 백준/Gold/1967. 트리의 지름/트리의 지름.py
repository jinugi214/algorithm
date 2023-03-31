'''
문제를 풀이 진행 방식
1. 트리에서 아무 노드나 잡고 그 노드에 대한 가장 먼 노드를 구하고 이 노드를 n1이라고 하자.
2. n1 에대한 가장 먼 노드를 한번 더 구한다. 이 노드를 n2라고 하자.
3. 이제 n1과 n2의 거리가 트리의 지름이 된다.

문제 코드 과정
1. 입력 받은 인풋으로 트리를 구현한다.
2. 트리에서 루트노드에서 가장 먼 노드를 dfs로 구한다.
3. 2번에서 구한 가장 먼 노드에서 한번 더 가장 먼 노드를 dfs로 구한다.
4. 3번에서 구한 가장 먼 길이가 정답이 된다.
'''
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

tree = [[] for _ in range(n+1)] # 노드를 담아주자

# 트리에서 루트노드에서 가장 먼 노드를 dfs로 구한다.
def dfs(x, val):
    for i in tree[x]:
        # 현재 노드와 연결된 자식 노드들
        s, v = i # 자식노드와 간선의 가중치
        if distance[s] == -1: # 거리가 아직 설정되어 있지않다면
            distance[s] = v + val # 트리에서 현재 노드까지의 거리를 설정
            dfs(s, val + v) # 계속해서 탐색


# 트리 구현
for _ in range(n-1):
    # 부모노드 번호, 자식노드 번호, 간선의 가중치
    p, s, v = map(int, input().split())

    # 양쪽 다 연결되어 있기 때문에
    tree[p].append([s, v])
    tree[s].append([p, v])

distance = [-1] * (n + 1)
distance[1] = 0 # 트리부분은 거리 0
dfs(1, 0) # 트리인 1에서 출발

# 트리에서 가장 먼 곳을 시작으로 하여 가장 먼 곳을 찾아보자
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))