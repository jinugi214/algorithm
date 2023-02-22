n, m = map(int, input().split())

data = []

for _ in range(n):
    data.append(input())

result = []

# 최적의 8x8 크기의 체스판을 자르기 위해 n-7을 이용해 구간을 순차적으로 확인한다.
for i in range(n-7):
    for j in range(m-7):
        w = 0
        b = 0
        for k in range(i, i+8):
            for l in range(j , j + 8):
                # 행과 열 인덱스의 합이 짝수, 홀수에 따라 값을 더한다.
                if (k + l) % 2 == 0:
                    if data[k][l] != 'W':
                        w = w + 1
                    if data[k][l] != 'B':
                        b = b + 1
                else:
                    if data[k][l] != 'B':
                        w = w + 1
                    if data[k][l] != 'W':
                        b = b + 1
        # 첫번째 색이 W인 경우와 B인 경우 둘 다 값을 넣는다.
        result.append(w)
        result.append(b)
# 두 색깔 중 최솟값을 구한다.
print(min(result))