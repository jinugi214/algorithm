import sys
import heapq

def dijkstra(start, arr):
    q = []
    arr[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        cost, now = heapq.heappop(q)
        if cost > arr[now]:
            continue
        arr[now] = cost
        for nextc, nextd in node_d[now]:
            heapq.heappush(q, (nextc+cost, nextd))


input = sys.stdin.readline
N, E = map(int, input().split())
node_d = {n: [] for n in range(1, N+1)}
for _ in range(E):
    a, b, c = map(int, input().split())
    node_d[a].append((c, b))
    node_d[b].append((c, a))
v1, v2 = map(int, input().split())
fromone = [10**9]*(N+1)
fromv1 = [10**9]*(N+1)
fromv2 = [10**9]*(N+1)
dijkstra(1, fromone)
dijkstra(v1, fromv1)
dijkstra(v2, fromv2)
case1 = fromone[v1]+fromv1[v2]+fromv2[N]
case2 = fromone[v2]+fromv2[v1]+fromv1[N]
ans = min((case1, case2))
if ans >= 10**9:
    print(-1)
else:
    print(ans)
