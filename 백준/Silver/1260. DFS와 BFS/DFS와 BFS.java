import java.util.*;


public class Main {
    static int N;
    static boolean[] visited;
    static ArrayList<Integer>[] graph;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        int M = sc.nextInt();
        int V = sc.nextInt();
        sc.nextLine();

        graph = new ArrayList[N+1];
        for(int i = 1; i <= N; i++){
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph[a].add(b);
            graph[b].add(a);
        }

        for (int i = 1; i <= N; i++) {
            Collections.sort(graph[i]);
        }

        visited = new boolean[N+1];
        dfs(V);
        System.out.println();

        visited = new boolean[N+1];
        bfs(V);
    }

    static void dfs(int num){
        System.out.print(num + " ");
        visited[num] = true;
        for (int next : graph[num]) {
            if (!visited[next]) {
                dfs(next);
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
            for (int next : graph[num]) {
                if (!visited[next]) {
                    queue.add(next);
                    visited[next] = true;
                }
            }
        }
    }
}