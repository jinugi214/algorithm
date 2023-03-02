import sys

input = sys.stdin.readline

N, K = map(int, input().split())
# 학생 수를 나타내는 정수 N
# 한 방에 배정할 수 있는 최대 인원 수 K
room = [[0] * 2 for _ in range(7)]
for i in range(N):
    S, Y = map(int, input().split())
    # S는 0, 1중 하나로서 여학생인 경우에 0, 남학생인 경우에 1
    # 학년 Y
    if S == 0: # 여학생
        room[Y][0] += 1
    if S == 1: # 남학생
        room[Y][1] += 1

cnt = 0

for i in range(1, 7):
    for j in range(2):
        if room[i][j] == 0:
            continue
        elif room[i][j] > K:
            if room[i][j] % K == 0:
                cnt += room[i][j] // K
            else:
                cnt += room[i][j] // K + 1
        else:
            cnt += 1

print(cnt)