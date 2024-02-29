import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] nums = new int[N+1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 1; i <= N; i++){
            nums[i] = Integer.parseInt(st.nextToken());
        }

        // 시간복잡도 O(N)
        // 100000(99999) / 2 = 대략 50억
        long cnt = 0;

        int idx = 1, distance = 1;

        boolean[] visited = new boolean[100001];

        // idx에서 시작해서 조건에 만족하면 distance를 늘려가자
        while(idx <= N){
            // 범위확인 및 처음 사용하는 숫자인지 확인
            while(distance <= N && !visited[nums[distance]]){
                visited[nums[distance]] = true; // 수 사용처리
                distance += 1;
            }

            // ex) 거리 3의 1,2,3 수열이면 1, 1,2, 1,2,3 수열
            cnt += (distance - idx);

            visited[nums[idx]] = false;
            idx += 1; // 다음 idx+1 시작
        }
        System.out.println(cnt);

    }
}