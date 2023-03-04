w, h = map(int, input().split())

data = [[1] * w for _ in range(h)]

N = int(input())

width = [0, w]  # 인덱스 시작 지점 0과 마지막 지점 넣어두기
height = [0, h]

for _ in range(N):
    type, num = map(int, input().split())
    # 0은 가로로 자르는 점선
    if type == 0:
        height.append(num)
    # 1은 세로로 자르는 점선
    elif type == 1:
        width.append(num)

width.sort()
height.sort()

ans = 0

for i in range(len(width) - 1):
    for j in range(len(height) - 1):
        x = width[i + 1] - width[i]
        y = height[j + 1] - height[j]
        ans = max(ans, x * y)

print(ans)
