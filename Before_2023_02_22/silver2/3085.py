import sys

input = sys.stdin.readline
n = int(input())
data = [list(input()) for _ in range(n)]

max_cnt = 0

def check_cnt():
    global max_cnt
    for i in range(n):
        cnt = 1
        for j in range(1, n): # 행 검사
            if data[i][j] == data[i][j - 1]:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1
        cnt = 1
        for j in range(1, n): # 열 검사
            if data[j][i] == data[j - 1][i]:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1
                
for i in range(n):
    for j in range(n):
        if j + 1 < n and data[i][j+1] != data[i][j]: # 행 검사
            data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
            check_cnt()
            data[i][j], data[i][j+1] = data[i][j+1], data[i][j]   
        if i + 1 < n and data[i + 1][j] != data[i][j]: # 열 검사
            data[i][j], data[i + 1][j] = data[i + 1][j], data[i][j] 
            check_cnt()
            data[i][j], data[i + 1][j] = data[i + 1][j], data[i][j]
        

print(max_cnt)

'''
N이 최대 50이므로 완전 탐색으로 한다.
한 위치에서 상하좌우가 아닌 아래와 오른쪽만 바꿔주면 된다.
바꾼 뒤에 가장 긴 연속 부분(행 또는 열)을 구한 뒤 원상복구 해주고
다음 걸로 계속 넘어가면서 반복해준다.

'''