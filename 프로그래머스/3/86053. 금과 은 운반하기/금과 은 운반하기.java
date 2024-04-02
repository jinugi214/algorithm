import java.util.*;

class Solution {
    public long solution(int a, int b, int[] g, int[] s, int[] w, int[] t) {
        long answer = -1;
        
        // 시간당 운반 가능 물품 계산하기
        long left = 1;
        long right = (long)(10e9 * 2 * 10e5 * 2); // 최대금 * 최대은 * 왕복시간
        int len = w.length;
        
        while(left<=right){
            long mid = (left + right) / 2; // 체크해볼 운반 시간
            int gold = 0, silver = 0, sum = 0;
            for(int i = 0; i < len; i++){
                int weight = w[i];
                int time = t[i];
                
                // 왕복 가능 횟수 체크
                long cnt = mid / (time * 2);
                if(mid % (time * 2) >= time){
                    cnt++;
                }
                
                gold += Math.min(g[i], weight * cnt); // 금 운반 가능량
                silver += Math.min(s[i], weight * cnt); // 은 운반 가능량
                sum += Math.min(g[i] + s[i], weight * cnt); // 금 + 은 운반 가능량
            }
            
            // 운반 가능하면 시간 줄이기
            if(gold >= a && silver >= b && sum >= a+b){
                answer = mid;
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }
        
        
        return answer;
    }
}