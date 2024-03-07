import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int[] nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        nums = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i<N; i++){
            nums[i] = Integer.parseInt(st.nextToken());
        }

        // 다른 수 2개의 합이 불가하기에
        if(nums.length < 3){
            System.out.println(0);
            return;
        }

        int cnt = 0;
        Arrays.sort(nums);
        for(int i = 0; i < N; i++){
            int start = 0;
            int end = N - 1;
            while(true){
                if(i == start) start++;
                else if (i == end) end--;

                if(start >= end) break;

                if(nums[start] + nums[end] < nums[i]) start++;
                else if(nums[start] + nums[end] > nums[i]) end--;
                else {
                    cnt++;
                    break;
                }
            }
        }
        System.out.println(cnt);

    }
}