import sys

input = sys.stdin.readline

n = int(input())

d = [list(map(int, input().split())) for _ in range(n)]

INF = 1e9

ans = 1e9

dp = [[0] * 3 for _ in range(2)] # 각 집이 색깔(빨, 초, 파)로 칠해졌을 때의 최소 비용

for i in range(3): # 빨, 초, 파 각각 시작하는 경우
    # 첫번째 집 초기화 
    dp[0][0], dp[0][1], dp[0][2] = INF, INF, INF
    dp[0][i] = d[0][i]
    
    for j in range(1, n): # 두번째 집부터 색깔을 다르게
        dp[1][0] = min(dp[0][1], dp[0][2]) + d[j][0]
        dp[1][1] = min(dp[0][0], dp[0][2]) + d[j][1]
        dp[1][2] = min(dp[0][0], dp[0][1]) + d[j][2]
        
        # 비용이 더해진 현재 집을 이전 집으로 바꾸기 위해서
        dp[0][0], dp[0][1], dp[0][2] = dp[1][0], dp[1][1], dp[1][2]
    
    # 첫번째 집과 같은 색깔이 아닌 비용을 찾기 위해 +1, +2 후 % 3 해준다.    
    ans = min(ans, min(dp[0][(i + 1) % 3], dp[0][(i + 2) % 3]))

print(ans)