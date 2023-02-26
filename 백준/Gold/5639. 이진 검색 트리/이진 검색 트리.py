# 트리를 만들고 후위 순회하면 시간초과 발생
# 전위 순회를 바로 후위 순회로 바꿔서 출력
import sys
sys.setrecursionlimit(10**9)
def postorder(s, e):
    if s > e:
        return

    for i in range(s + 1, e + 1):
        if nums[s] < nums[i]:  # 루트보다 크면 오른쪽 노드
            mid = i
            break
    else:
        mid = e + 1  # 루트보다 큰 오른쪽이 없는 경우

    postorder(s + 1, mid - 1)  # 재귀로 왼쪽 트리 노드 출력
    postorder(mid, e)  # 재귀로 오른쪽 트리 노드 출력
    print(nums[s])  # 마지막 루트 출력


nums = []
while True:
    try:  # 입력을 있을 때만 입력받기
        nums.append(int(sys.stdin.readline()))
    except:
        break

postorder(0, len(nums) - 1)
