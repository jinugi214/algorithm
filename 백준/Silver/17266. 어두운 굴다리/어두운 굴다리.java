import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] slamp = new int[M]; // 가로등 위치
        for(int i = 0; i<M; i++){
            int temp = Integer.parseInt(st.nextToken());
            slamp[i] = temp;
        }

        int ans = 0; // 높이

        int low = 1;
        int high = N;
        // 이진 탐색
        while(low <= high){
            int mid = (low + high) / 2;
            boolean flag = true;

            // mid 값으로 가능한지 확인
            int prev = 0; // 이전에 비추던 최대 위치 (처음부터 비춰야하기 때문에 0)
            for (int i = 0; i<M; i++){
                if(slamp[i] - mid <= prev){
                    prev = slamp[i] + mid; // 가로등은 prev까지 비출수 있다.
                }
                else {
                    flag = false;
                }
            }
            if(N - prev > 0){ // 끝부분 부터 한번 더 확인
                flag = false;
            } else{
                flag = true;
            }

            if(flag) { // 거리 모두 비추기 가능
                ans = mid;
                high = mid - 1;
            } else { // 거리 모두 비추기 불가능
                low = mid + 1;
            }
        }

        System.out.println(ans);

    }
}