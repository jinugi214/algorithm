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

            int prev = 0;
            for (int i = 0; i<M; i++){
                if(slamp[i] - mid <= prev){
                    prev = slamp[i] + mid; // 가로등은 light까지 비출수 있다.
                }
                else {
                    flag = false;
                }
            }
            if(N - prev > 0){
                flag = false;
            } else{
                flag = true;
            }

            if(flag) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        System.out.println(ans);

    }
}