import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N;
    static int M;
    static int[][] cities;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine()); // 도시 수
        M = Integer.parseInt(br.readLine()); // 여행 계획에 속한 도시 수

        cities = new int[N+1][N+1];

        StringTokenizer st;
        for(int i = 1; i<=N; i++){
            // a와 b 도시 연결
            st = new StringTokenizer(br.readLine());
            for(int j = 1; j<=N; j++){
                String val = st.nextToken();
                if (val.equals("1")){
                    cities[i][j] = 1;
                    cities[j][i] = 1;
                }
            }
        }

        // 여행 계획
        Queue<Integer> q = new LinkedList<>();
        st = new StringTokenizer(br.readLine());
        for(int j = 1; j<=M; j++){
             int city = Integer.parseInt(st.nextToken());
             q.add(city);
        }

        String answer = "";

        if(M == 1){
            answer = "YES";

        }
        else {
            int cur = q.poll();
            boolean result = true;
            while(!q.isEmpty()){
                int d = q.poll();
                if (dfs(cur, d, new boolean[N + 1])){
                    cur = d;
                } else {
                    answer = "NO";
                    result = false;
                    break;
                }
            }
            if (result){
                answer = "YES";
            }
        }

        System.out.println(answer);


    }

    static boolean dfs(int cur, int end, boolean[] visited){
        if(cur == end){
            return true;
        }

        visited[cur] = true;

        for(int i = 1; i <= N; i++){
            if (cities[cur][i] == 1 && !visited[i]){
                boolean go = dfs(i, end, visited);
                if (go) return true;
            }
        }

        return false;
    }
}