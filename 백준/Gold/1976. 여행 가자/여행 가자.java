import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N;
    static int M;
    static int[] cities;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine()); // 도시 수
        M = Integer.parseInt(br.readLine()); // 여행 계획에 속한 도시 수

        cities = new int[N + 1];

        for(int i = 1; i <= N; i++){
            cities[i] = i;
        }

        StringTokenizer st;
        for(int i = 1; i<=N; i++){
            // a와 b 도시 연결
            st = new StringTokenizer(br.readLine());
            for(int j = 1; j<=N; j++){
                if(st.nextToken().equals("1")){
                    union(i, j);
                }
            }
        }

        // 여행 계획
        int[] plan = new int[M];
        st = new StringTokenizer(br.readLine());
        for(int j = 0; j<M; j++){
            plan[j] = Integer.parseInt(st.nextToken());
        }

        String answer = "YES";

        for(int i = 0; i <M-1; i++){
            if (find(plan[i]) != find(plan[i + 1])){
                answer = "NO";
                break;
            }
        }
        System.out.println(answer);


    }

    static int find(int x) {
        if (x == cities[x]) {
            return x;
        } else {
            return cities[x] = find(cities[x]);
        }
    }

    static void union(int x, int y) {
        x = find(x);
        y = find(y);
        if (x != y) {
            cities[y] = x;
        }
    }
}