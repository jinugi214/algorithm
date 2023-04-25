def comb(arr, n): # 재귀를 이용한 조합
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result. append([i])
    elif n > 1:
        # arr의 첫 번째 요소를 선택하고
        for i in range(len(arr) - n + 1):
            # 나머지 요소들 중에서 n-1개를 선택하는 모든 조합을 구하여 result에 추가
            for j in comb(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)
    return result

N = int(input())

nums = [i for i in range(0, 10)]

data = []
# 9876543210 총 10자리니까 1~11
for i in range(1, 11):
    for j in comb(nums, i):
        num = sorted(list(j), reverse=True) # 조합을 나온 수들을 내림차순으로 정렬
        data.append(int(''.join(map(str, num)))) # 값들을 한곳에 담아주자

data.sort() # 길이별 정렬

if len(data) > N: # 해당 감소하는 수가 있다면
    print(data[N])
else:
    print(-1)
