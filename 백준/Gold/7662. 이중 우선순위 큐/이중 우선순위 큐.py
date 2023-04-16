from heapq import heappop, heappush
import sys

input = sys.stdin.readline


def check(arr): # 최소힙과 최대힙의 상태를 동기화 시켜주자
    while arr and idx[arr[0][1]] == 0:
        heappop(arr)


T = int(input())

for t in range(T):
    idx = [0] * 1000000  # 삭제 동기화를 위한 배열
    # heap에서 최대값 최솟값을 둘다 다루기 위해서 최대힙, 최소힙 두개를 만들어주자
    maxq = []
    minq = []
    k = int(input())
    for i in range(k):
        c, n = input().split()
        n = int(n)
        if c == 'I':
            heappush(maxq, (-n, i))
            heappush(minq, (n, i))
            idx[i] = 1
        elif c == 'D':
            if n == 1:
                check(maxq)
                if maxq:
                    idx[maxq[0][1]] = 0
                    heappop(maxq)
            elif n == -1:
                check(minq)
                if minq:
                    idx[minq[0][1]] = 0
                    heappop(minq)

    # 연산이 끝난 후 아직 처리되지 못한 것들을 동기화 시켜주자
    check(maxq)
    check(minq)

    if not maxq:
        print('EMPTY')
    else:
        print(-1 * maxq[0][0], minq[0][0])
