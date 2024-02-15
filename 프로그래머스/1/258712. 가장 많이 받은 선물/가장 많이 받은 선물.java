import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        
        HashMap<String, Integer> idx = new HashMap<>();
        
        for (int i = 0; i < friends.length; i++){
            idx.put(friends[i], i);
        }
        
        int c = friends.length;
        
        int[][] give = new int[c][c];
        int[][] take = new int[c][c];
        
        for (String g : gifts){
            String[] tmp = g.split(" ");

            give[idx.get(tmp[0])][idx.get(tmp[1])] += 1;
            take[idx.get(tmp[1])][idx.get(tmp[0])] += 1;
        }
        
        int[] giftNum = new int[c];
        
        for(int i = 0; i < c; i++){
            giftNum[i] = Arrays.stream(give[i]).sum() - Arrays.stream(take[i]).sum();
        } 
        
        int[] nextGift = new int[c]; 
        
        // 가장 많은 선물을 받는 친구를 계산하자
        // 서로 주고 받은 기록이 없거나 비교해서 차이가 0이면 선물지수가 더 큰사람이 받는다.
        
        for(int i = 0; i < c; i++){
            for(int j = 0; j < c; j++){
                if (i == j){
                    continue;
                } else {
                    if (give[i][j] > take[i][j]) {
                        nextGift[i] += 1;
                    } else if (give[i][j] == take[i][j]) {
                        if (giftNum[i] > giftNum[j]) {
                            nextGift[i] += 1;
                        }
                    } 
                }
            }
        }
        
        int answer = Arrays.stream(nextGift).max().getAsInt();
        
        return answer;
    }
}