
N, M = map(int, input().split())

if N == 1: # 세로가 1일 경우 시작지점만 방문
    print(1)
elif N == 2: # 세로가 2일 경우 2, 3번만 이동 가능
    print(min(4, (M-1)//2+1))
elif M <= 6: # 가로가 6보다 작거나 같으면 1, 4번만 이동 가능
    print(min(4, M))
else: # 모든 방법을 쓸 수 있으면 가로길이 - 2가 최댓값
    print(M-2)