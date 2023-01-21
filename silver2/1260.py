from collections import deque
import sys

input = sys.stdin.readline

def dfs(v):
    #방문한 곳은 1
    visit_dfs[v] = 1
    print(v, end = " ")
    
    # 인접한 곳 중 방문하지 않은 곳을 찾고 재귀함수 실행
    for i in range(1, n + 1):
        # 방문하지 않은 곳과 graph[v]에서 낮은 숫자부터 연결된 곳 우선 방문
        if visit_dfs[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    visit_bfs[v] = 1
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n + 1):
            if visit_bfs[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit_bfs[i] = 1

# 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V
n, m, v = map(int, input().split())


graph = [[0] * (n + 1) for _ in range(n + 1)]

# 방문한 곳 체크를 위한 배열
visit_dfs = [0] * (n + 1)
visit_bfs = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    # 양방향이기에 [b][a]도 1이다.
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)