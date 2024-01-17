import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;


public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();

        int[] visited = new int[100001];

        bfs(N, K, visited);
    }

    static void bfs(int N, int K, int[] visited) {

        Queue<Integer> queue = new LinkedList<>();

        queue.add(N);

        while (!queue.isEmpty()) {
            int cur = queue.poll();

            if (cur == K) {
                System.out.println(visited[K]);
                break;
            }

            for (int i = 0; i < 3; i++) { // i가 0일 때는 -1, 1일 때는 +1, 1일 때는 *2
                if (i == 0 && cur - 1 >= 0 && visited[cur - 1] == 0) {
                    queue.add(cur - 1);
                    visited[cur - 1] = visited[cur] + 1;
                } else if (i == 1 && cur + 1 <= 100000 && visited[cur + 1] == 0) {
                    queue.add(cur + 1);
                    visited[cur + 1] = visited[cur] + 1;
                } else if (i == 2 && cur * 2 <= 100000 && visited[cur * 2] == 0) {
                    queue.add(cur * 2);
                    visited[cur * 2] = visited[cur] + 1;
                }
            }

        }

    }
}