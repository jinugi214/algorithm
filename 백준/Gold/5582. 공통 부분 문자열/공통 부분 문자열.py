a = input()
b = input()

la = len(a) + 1
lb = len(b) + 1

# dp 테이블
dp = [[0] * lb for _ in range(la)]

mv = 0

for i in range(1, la):
    for j in range(1, lb):
        # 문자가 같다면
        if a[i-1] == b[j-1]:
            # 대각선으로 가면서 가장 긴 길이
            dp[i][j] = dp[i-1][j-1] + 1
            # 가장 긴 길이
            mv = max(mv, dp[i][j])

print(mv)