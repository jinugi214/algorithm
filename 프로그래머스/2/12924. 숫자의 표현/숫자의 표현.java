class Solution {
    public int solution(int n) {
                    
        int answer = 0;
        for(int i = 1; i <= n; i++){ // 시작점
            int sum = 0;
            for (int j = i; j <= n; j++){ // 연속한 자연수
                sum += j;
                
                if(sum == n){
                    answer++;
                    break;
                } else if (sum > n) {
                    break;
                }
            }
        }
        
        return answer;
        
        
    }
}