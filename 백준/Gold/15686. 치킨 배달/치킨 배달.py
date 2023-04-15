import sys

input = sys.stdin.readline

# N개의 줄에서 최대 M개를 고르고 모두 폐업시키기
N, M = map(int, input().split())

# 0은 빈 칸, 1은 집, 2는 치킨집을 의미
data = [list(map(int, input().split())) for _ in range(N)]

# 도시의 치킨 거리가 가장 작게 될지 구하자
# 지도에서 치킨집 M개만 두는 경우를 모두 고려하여 (조합)
# 1을 만날 때마다 가장 가까운 2까지 거리를 계산해서 모두 더하기
# 그리고 값을 비교하기

chicken = []
home = []
# 우선 그냥 집과 치킨집을 모두 찾아보자
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            home.append((i, j))
        elif data[i][j] == 2:
            chicken.append((i, j))


def comb(arr, n):  # 조합
    rlt = []
    if n > len(arr):  # 원하는 개수보다 배열의 길이가 작으면
        return rlt  # 그대로 반환

    if n == 1:  # 원하는 개수가 1개면 하나씩 순회해서 반환
        for i in arr:
            rlt.append([i])
    elif n > 1:  # 원하는 개수가 1개보다 크면
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1:], n - 1):
                rlt.append([arr[i]] + j)
    return rlt

# 치킨집 거리 비교
def check(chicken):
    val = 0
    for h in home:
        hx, hy = h
        tmp = 1e9
        for c in chicken:
            cx, cy = c
            tmp = min(abs(hx-cx) + abs(hy-cy), tmp)
        val += tmp
    return val

chicken = comb(chicken, M)

min_val = 1e9

for i in chicken:
    tmp = check(i)
    min_val = min(min_val, tmp)

print(min_val)