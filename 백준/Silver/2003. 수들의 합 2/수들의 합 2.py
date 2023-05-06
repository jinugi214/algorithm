N, M = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 1
cnt = 0
while right<=N and left<=right:

    num_lst = nums[left:right]
    total = sum(num_lst)

    if total == M:
        cnt += 1

        right += 1

    elif total < M:
        right += 1

    else:
        left += 1

print(cnt)