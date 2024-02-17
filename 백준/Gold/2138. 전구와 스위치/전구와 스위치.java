import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N;
    static int[] firstLights, secondLights, target;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        // i번 스위치는 i-1 전구 상태가 정답의 i-1 상태와 일치한다면 누르지 않는다.
        // 1번 스위치는 0번 스위치가 없기 때문에 누른 경우와 누르지 않은 경우 2개로 시작
        char[] lights = br.readLine().toCharArray();

        firstLights = new int[N];
        secondLights = new int[N];

        for (int i = 0; i < N; i++){
            firstLights[i] = lights[i] - '0'; // ASCII 코드로 정수 변환
            secondLights[i] = lights[i] - '0';
        }

        firstLights[0] ^= 1; // 토글연산 0 -> 1  1 -> 0
        firstLights[1] ^= 1;

        lights = br.readLine().toCharArray();

        target = new int[N];

        for(int i = 0; i < N; i++){
            target[i] = lights[i] - '0';
        }

        int firstLightsCnt = change(firstLights) + 1;
        int secondLightsCnt = change(secondLights);

        if(!check(firstLights) && !check(secondLights)){
            System.out.println(-1);
        }
        else if (check(firstLights) && !check(secondLights)){
            System.out.println(firstLightsCnt);
        }
        else if(!check(firstLights) && check(secondLights)){
            System.out.println(secondLightsCnt);
        }
        else{
            System.out.println(Math.min(firstLightsCnt, secondLightsCnt));
        }



    }

    static int change(int[] lights){
        int ans = 0;
        for (int i = 1; i < N; i++){
            if(lights[i-1] != target[i-1]){ // 정답과 다르면 스위치 누르기
                lights[i-1] ^= 1;
                lights[i] ^= 1;
                if(i + 1 < N){
                    lights[i + 1] ^= 1;
                }
                ans++;
            }
        }
        return ans;
    }

    static boolean check(int[] lights){ // 목표값과 같은지 확인
        for(int i = 0; i < N; i++){
            if(lights[i] != target[i]){
                return false;
            }
        }
        return true;
    }
}