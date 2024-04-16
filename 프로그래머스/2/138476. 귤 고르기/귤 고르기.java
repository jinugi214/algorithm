import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        
        int mv = Arrays.stream(tangerine).max().getAsInt();
        
        int[] vals = new int[mv];
        for(int t : tangerine){
            vals[t-1] += 1;
        }
        int answer = 0;
        Arrays.sort(vals);
        for(int i = vals.length - 1; i>=0; i--){
            k -= vals[i];
            answer++;
            if(k <= 0){
                break;
            }
        }
        return answer;
    }
}