class Solution {
    public int solution(int[][] matrix_sizes) {
        int n = matrix_sizes.length;
        int[][] dp = new int[n][n]; // 최소 연산 횟수 담는 곳
        
        for(int i = 0; i < n; i++){
            dp[i][i] = 0;
        }
        
        for(int i = 1; i < n; i++){
            for(int start = 0; start < n - i; start++){
                int end = start + i;
                dp[start][end] = Integer.MAX_VALUE; // 최댓값 설정
                
                for(int fixed = start; fixed < end; fixed++){
                    // fixed를 기준으로 왼쪽부분의 최소 연산횟수와 오른쪽 부분의 최소 연산횟수
                    // 그리고 두 부분을 곱하는 데 필요한 연산 횟수를 고려하여 최소값을 갱신
                    dp[start][end] = Math.min(dp[start][end], dp[start][fixed] + dp[fixed +1][end] + matrix_sizes[start][0] * matrix_sizes[fixed + 1][0] * matrix_sizes[end][1]);
                }
            }
        }
        
        return dp[0][n-1];
    }
}