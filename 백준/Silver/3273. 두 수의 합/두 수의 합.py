n = int(input())

data = list(map(int, input().split()))

x = int(input())

left = 0
right = len(data) - 1

# 정렬
data.sort()

# 횟수
ans = 0

while left < right:  # 왼쪽과 오른쪽이 만날 때까지 반복
    val = data[left] + data[right]
    if val == x:  # 왼쪽 + 오른쪽 = x 만족하는 쌍
        ans += 1
        left += 1
        right -= 1
    elif val < x:  # 값이 작으면
        left += 1  # 왼쪽값 올리기 (오름차순 정렬이라 더 큰 값이 필요해서)
    else:  # 값이 크면
        right -= 1  # 오른쪽 값 내리기 (오름차순 정렬이라 더 작은 값이 필요해서)

print(ans)
