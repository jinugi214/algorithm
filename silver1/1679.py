import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k: # 원하는 곳에 도착
            print(data[x]) # 지금까지의 이동시간을 출력
            break 
        for y in (x - 1, x + 1, x * 2): # 세가지의 선택지
            if 0 <= y <= max_data and not data[y]: # 값이 조건안이고 이동시간이 0이면
                data[y] = data[x] + 1 # 이동시간 1 증가
                q.append(y) # 다음 값을 찾기 위한 반복을 위해 추가 

max_data = 10** 5 # 문제에서 제시한 제한값 (시간초과 방지)
data = [0] * (max_data + 1) # 이동 시간을 담는 곳
n, k = map(int, input().split())

bfs()