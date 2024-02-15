import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        int[] array = new int[N];
        int idx = 0;
        while(st.hasMoreTokens()){
            array[idx] = Integer.parseInt(st.nextToken());
            idx++;
        }

        int left = 0;
        int right = 0;

        int answer = N + 1;
        int val = array[left];
        while(left <= right){
            if (val >= S){
                answer = Math.min(answer, right - left + 1);
                val -= array[left];
                left += 1;
            } else {
                right += 1;
                if (right >= N) break;
                val += array[right];
            }
        }

        if(answer == N + 1){
            answer = 0;
        }

        System.out.println(answer);
    }
}