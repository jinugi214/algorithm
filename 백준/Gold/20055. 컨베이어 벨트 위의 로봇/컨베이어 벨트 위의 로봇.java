import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        int N = Integer.parseInt(inputs[0]);
        int K = Integer.parseInt(inputs[1]);

        StringTokenizer st = new StringTokenizer(br.readLine());

        int len = 2 * N;

        int[] belt = new int[len];
        boolean[] robot = new boolean[N];



        for(int i = 0; i < len; i++){
            belt[i] = Integer.parseInt(st.nextToken());
        }

        // 내구도 0이 K개 이상이면 종료
        int result = 0;
        while(true){
            int broke = 0;
            for(int i=0; i<2*N; i++){
                if(belt[i]==0) broke++;
            }
            if(broke >= K){
                break;
            }


            // 1. 한칸 회전한다.
            int tmp = belt[len-1];
            for(int i = len-1; i > 0; i--){
                belt[i] = belt[i-1];
            }
            belt[0] = tmp;

            for(int i = N-1; i > 0; i--){
                robot[i] = robot[i-1];
            }
            robot[0] = false;
            robot[N-1] = false; // 로봇 내리기

            // 2. 가장 먼저 벨트에 올라간 로봇부터 이동가능하면 이동한다.
            for(int i = N-1; i>0; i--){
                if(!robot[i] && robot[i-1] && belt[i] > 0){
                    belt[i]--;
                    robot[i] = true;
                    robot[i - 1] = false;
                }
            }

            // 3. 올리는 위치에 칸의 내구도 0이 아니면 위치에 로봇을 올린다.
            if(belt[0] > 0){
                robot[0] = true;
                belt[0]--;
            }

            result++;

        }
        System.out.println(result);
    }
}