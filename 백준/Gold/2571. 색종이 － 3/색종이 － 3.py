n = int(input())

paper = [[0] * 101 for _ in range(101)]

# 도화지에 색종이 존재하는 곳 표시
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

# 누적합을 저장하면서 높이값 저장
for i in range(99):
    for j in range(100):
        if paper[i][j] != 0 and paper[i+1][j] != 0:
            paper[i + 1][j] = paper[i][j] + 1

mx = 0
for i in range(100):
    for j in range(100):
        h = 100
        # 현재 위치를 기준에서 오른쪽으로 가능한 높이를 구하기
        for k in range(j, 100):
            h = min(h, paper[i][k]) # 가로 위치의 값 중 최소값
            if h == 0: # 종이가 없는 위치
                break
            mx = max(mx, h * (k - j + 1)) # 사각형 최대 넓이 구하기
print(mx)