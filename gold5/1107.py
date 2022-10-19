import sys

input = sys.stdin.readline

# 목표 채널
n = int(input())

# 고장난 리모컨 개수
m = int(input())

if m:
    # 고장난 리모컨 버튼들
    error = list(input().split())
else:
    # 고장난거 없으면
    error = []

# 처음 100번 채널에서 +와 -로 이동할 경우 최댓값
ans = abs(100 - n)

# N (0 ≤ N ≤ 500,000)이지만 -로 채널을 찾을 수 도 있기에 1,000,000까지
for num in range(1000001):
    for x in str(num):
        if x in error: # 해당 번호가 고장난 번호이면
            break
    else: # 누를 수 있는 번호의 경우
        # 기존횟수, 번호 누른횟수 + 현재 번호부터 목표번호까지의 차이
        ans = min(ans, len(str(num)) + abs(num - n))

print(ans)