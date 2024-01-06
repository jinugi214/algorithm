import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;


public class Main {
    static int N;
    static boolean[] visited;
    static int[][] graph;
    static int M;
    static int V;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();
        V = sc.nextInt();
        sc.nextLine();

        visited = new boolean[N+1];
        visited[0] = true;
        graph = new int[N+1][N+1];

        for (int i = 0; i < M; i++){
            String input = sc.nextLine();
            String[] tmp = input.split(" ");
            int a = Integer.parseInt(tmp[0]);
            int b = Integer.parseInt(tmp[1]);
            graph[a][b] = 1;
            graph[b][a] = 1;
        }

        dfs(V);
        System.out.println();
        visited = new boolean[N+1];
        visited[0] = true;
        bfs(V);
    }

    static void dfs(int num){
        System.out.print(num + " ");
        visited[num] = true;
        for (int i = 1; i < N+1; i++){
            if(!visited[i] && graph[num][i] == 1){
                dfs(i);
            }
        }
    }
    static void bfs(int start){
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        visited[start] = true;
        while (!queue.isEmpty()){
            int num = queue.poll();
            System.out.print(num + " ");
            for (int i = 1; i < N+1; i++){
                if(!visited[i] && graph[num][i] == 1){
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }
    }
}