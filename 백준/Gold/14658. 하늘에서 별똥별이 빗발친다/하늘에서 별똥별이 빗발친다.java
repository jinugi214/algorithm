
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

    static List<int[]> stars;

    static int L;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] inputs = br.readLine().split(" ");

        int N = Integer.parseInt(inputs[0]); // 별똥별의 가로길이
        int M = Integer.parseInt(inputs[1]); // 별똥별의 세로길이
        L = Integer.parseInt(inputs[2]); // 트램펄린 한변길이
        int K = Integer.parseInt(inputs[3]); // 별똥별의 수

        stars = new ArrayList<>();

        // 별똥별 좌표
        for(int i = 0; i<K; i++){
            String[] starXY = br.readLine().split(" ");
            int x = Integer.parseInt(starXY[0]);
            int y = Integer.parseInt(starXY[1]);
            stars.add(new int[]{x, y});
        }


        int result = 0;
        for(int[] s1 : stars){
            for(int[] s2 : stars){
                result = Math.max(result, check(s1[0], s2[1]));
            }
        }
        System.out.println(K-result);
    }

    static int check(int sx, int ey){
        int cnt = 0;
        for(int[] s : stars){
            if(sx <= s[0] && s[0] <= sx + L && ey <= s[1] && s[1] <= ey + L ){
                cnt++;
            }
        }
        return cnt;
    }

}