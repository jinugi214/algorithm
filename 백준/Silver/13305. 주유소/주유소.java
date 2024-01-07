import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] way = new int[N - 1];

        for (int i = 0; i < N-1; i++) {
            way[i] = Integer.parseInt(st.nextToken());
        }

        int[] cost = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            cost[i] = Integer.parseInt(st.nextToken());
        }


        long minCost = cost[0]; // 최소 비용
        long sum = 0; // 총 비용

        for (int i = 0; i < N - 1; i++) {
            // 현재 도시의 기름 가격이 더 싸면 최소 비용 갱신
            if (cost[i] < minCost) {
                minCost = cost[i];
            }

            // (도로 길이 * 기름 가격)을 총 비용에 더함
            sum += (minCost * way[i]);
        }

        System.out.println(sum);

    }
}