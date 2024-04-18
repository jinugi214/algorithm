class Solution {
    public int solution(String dirs) {
        
        boolean[][][] visited = new boolean[11][11][4];
        
        int answer = 0;
        int x = 5;
        int y = 5;
        
        for(int i = 0; i < dirs.length(); i++){
            
            // U : 0, D : 1, L : 2, R : 3
            
            
            if(dirs.charAt(i) == 'U' && x < 10){
                x++;
                
                if(visited[x][y][0] == false){
                    visited[x][y][0] = true;
                    visited[x-1][y][1] = true;
                    answer++;
                }
                
            } else if(dirs.charAt(i) == 'D' && x > 0){
                x--;
                
                if(visited[x][y][1] == false){
                    visited[x][y][1] = true;
                    visited[x+1][y][0] = true;
                    answer++;
                }
                
            } else if(dirs.charAt(i) == 'L' && y > 0){
                y--;
                
                if(visited[x][y][2] == false){
                    visited[x][y][2] = true;
                    visited[x][y+1][3] = true;
                    answer++;
                }
            } else if(dirs.charAt(i) == 'R' && y < 10){
                y++;
                
                if(visited[x][y][3] == false){
                    visited[x][y][3] = true;
                    visited[x][y-1][2] = true;
                    answer++;
                }
            }
            
        }
                
        return answer;
        
    }
}