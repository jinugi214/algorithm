import sys

input = sys.stdin.readline


def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2  # 중간값 (절단기 높이)

        sum_v = 0  # 잘린 나무 총합
        for x in tree:
            if x > mid:
                sum_v += x - mid

        if sum_v >= M:
            start = mid + 1
            # 원하는 만큼 나무 길이를 충분히 얻었기 때문에 절단기 높이를 높이자
        else:
            end = mid - 1
            # 원하는 만큼 나무 길이를 얻지 못해 절단기 높이를 낮추자

    # 이분탐색 끝나고 결과값 반환
    return end


# 나무의 수 N, 집으로 가져가려고 하는 나무의 길이 M
N, M = map(int, input().split())

# 나무들의 길이
tree = list(map(int, input().split()))

max_v = max(tree)  # 절단기 높이 설정 최대값
min_v = 0  # 절단기 높이 설정 최소값

print(binary_search(min_v, max_v))
