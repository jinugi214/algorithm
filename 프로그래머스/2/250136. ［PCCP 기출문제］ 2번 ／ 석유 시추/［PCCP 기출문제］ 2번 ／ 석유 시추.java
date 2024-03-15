import java.util.*;

class Solution {
    public int solution(int[][] land) {

        int garo = land[0].length;
        int sero = land.length;
        Map<Integer, Integer> map = new HashMap<>();
        int[][] oils = new int[sero][garo];
        int[][] direct = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        int oilNum = 2;
        for(int i = 0; i<sero; i++){
            for(int j = 0; j<garo; j++){
                if(land[i][j] == 1){
                    int cnt = 1;
                    ArrayDeque<int[]> dq = new ArrayDeque<>();
                    dq.add(new int[]{i, j});
                    land[i][j] = oilNum;
                    while(!dq.isEmpty()){
                        int[] tmp = dq.poll();          
                        for(int k = 0; k<4; k++){
                            int nx = tmp[0] + direct[k][0];
                            int ny = tmp[1] + direct[k][1];              
                            if (nx >= 0 && nx < sero && ny >= 0 && ny < garo && land[nx][ny] == 1){
                                dq.add(new int[]{nx, ny});
                                land[nx][ny] = oilNum;
                                cnt++;
                            }
                        }
                    }
                    map.put(oilNum, cnt);
                    oilNum++;
                }
            }
        }
        
        int answer = 0;
        for(int y = 0; y<garo; y++){
            Set<Integer> set = new HashSet<>();
            for(int x = 0; x<sero; x++){
                if(land[x][y] > 1){
                    set.add(land[x][y]);
                }   
            }
            int val = 0;
            Iterator<Integer> iter = set.iterator();
            while(iter.hasNext()){
                val += map.get(iter.next());
            }
            answer = Math.max(answer ,val);
        }
        
        return answer;
    }
}