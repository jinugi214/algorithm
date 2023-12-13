from collections import deque

n = int(input())

nums = [0] * (n+1)

q = deque()
q.append([n, []])

while q:
    c, lst = q.popleft()
    if c == 1:
        print(nums[1])
        lst.append(1)
        print(*lst)

        break
    if c % 3 == 0 and nums[c//3] == 0:
        q.append([c // 3, lst + [c]])
        nums[c//3] = nums[c]+1
    if c % 2 == 0 and nums[c//2] == 0:
        q.append([c // 2, lst + [c]])
        nums[c // 2] = nums[c] + 1
    if nums[c - 1] == 0:
        q.append([c-1, lst + [c]])
        nums[c-1] = nums[c] + 1
