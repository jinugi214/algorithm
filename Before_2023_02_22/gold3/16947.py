import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def dfs(idx, cnt):
    if rotate[idx]:  # 방문한 노드라면
        if cnt - distance[idx] >= 3: # 거리차가 3이상이라면 사이클에 속한다.
            return idx  # 사이클 시작 정점 반환
        else:
            return -1

    # 방문하지 않은 노드이면
    rotate[idx] = 1  # 방문처리
    distance[idx] = cnt  # 현재까지의 거리

    for y in route[idx]:  # 인덱스와 연결된 노선을 순회
        cycleStartNode = dfs(y, cnt + 1)  # 연결된 노선을 재귀한 결과

        if cycleStartNode != -1:
            rotate[idx] = 2  # 사이클로 등록
            if idx == cycleStartNode: # 사이클이 시작된 곳과 같은 인덱스면
                return -1
            else:
                return cycleStartNode

    return -1


if __name__ == '__main__':
    N = int(input())
    route = [[] * N for _ in range(N)]
    # rotate[i] = 0 : 방문하지 않은 노드
    # rotate[i] = 1 : 방문한 노드
    # rotate[i] = 2 : 사이클에 속하는 노드
    rotate = [0] * N  # 순환선
    distance = [0] * N  # 거리

    for _ in range(N):  # 루트 입력
        a, b = map(int, input().split())
        route[a - 1].append(b - 1)
        route[b - 1].append(a - 1)

    dfs(1, 0)  # 1번 노선부터 출발

    queue = deque()
    for i in range(N):
        if rotate[i] == 2:  # 사이클이면
            queue.append(i)
            distance[i] = 0

        else:  # 사이클이 아니면
            distance[i] = -1

    while queue:
        now = queue.popleft()

        for y in route[now]:
            if distance[y] == -1:
                queue.append(y)  # 사이클에서의 거리를 +1 씩 더해준다.
                distance[y] = distance[now] + 1

    print(*distance)
