import java.util.*;

class Solution {
    
    int[] node;
    List<Integer>[] graph = new ArrayList[17];
    boolean[][][] visited; // 노드, 양, 늑대에 따른 경우의 수 방문처리
    int answer;
    
    public int solution(int[] info, int[][] edges) {
        node = info;
        for (int i = 0; i < node.length; i++){
            graph[i] = new ArrayList<>();
        }
        
        for(int[] edge : edges){
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }
        
        visited = new boolean[17][17][17];
        answer = 0;
        dfs(0, 0, 0);
        
        return answer;
        
    }
    
    void dfs(int cur, int sheep, int wolf){
        if(visited[cur][sheep][wolf]) return;
        visited[cur][sheep][wolf] = true;
        
        int bs = sheep, bw = wolf;
        int bn = node[cur];
        
        if(node[cur] == 0)
            sheep++;
        else if (node[cur] == 1)
            wolf++;
        
        node[cur] = -1;
        
        if (wolf < sheep){
            answer = Math.max(answer, sheep);
            for (int next : graph[cur]){
                dfs(next, sheep, wolf);
            }
        }
        
        // 탐색 후 이전 값으로 복원
        node[cur] = bn;
        visited[cur][bs][bw] = false;
    }
    
}