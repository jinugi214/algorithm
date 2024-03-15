import java.lang.*;
import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] oneP = {1, 2, 3, 4, 5};
        int[] twoP = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] threeP = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int[] pars = new int[4];
        
        for(int i = 0; i < answers.length; i++){
            int ans = answers[i];
            if(oneP[i % oneP.length] == ans) pars[1]++;
            if(twoP[i % twoP.length] == ans) pars[2]++;
            if(threeP[i % threeP.length] == ans) pars[3]++;
        }
        
        int maxV = Math.max(Math.max(pars[1], pars[2]), pars[3]);
        List<Integer> result = new ArrayList<>();
        for(int i = 1; i<4; i++){
            if(maxV == pars[i]) result.add(i);
        }
        
        return result.stream().mapToInt(i -> i).toArray();
    }
}