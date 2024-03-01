import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for(int tc = 0; tc < T; tc++){

            String W = br.readLine();
            int K = Integer.parseInt(br.readLine());

            if(K == 1) { //k가 1일때
                System.out.println("1 1");
                continue;
            }

            int[] alpha = new int[26];

            // 알파벳 개수 저장
            for(char c : W.toCharArray()){
                alpha[c-'a'] += 1;
            }

            int minLen = 10001;
            int maxLen = -1;

            // 같은 문자가 있는 가장 짧은 연속 문자열은 결국 (시작문자 = 마지막문자)
            for(int i = 0; i < W.length(); i++){
                // 시작 문자가 K 개수보다 적으면 pass
                if(alpha[W.charAt(i) - 'a'] < K) continue;

                int cnt = 1;
                for(int j = i + 1; j < W.length(); j++){
                    if(W.charAt(j) == W.charAt(i)) cnt++;
                    if(cnt == K){
                        minLen = Math.min(minLen, j-i+1);
                        maxLen = Math.max(maxLen, j-i+1);
                        break; // K개 포함된 것 확인되면 중단 (시작문자 = 마지막 문자)
                    }
                }
            }
            if(minLen == 10001 || maxLen == -1) System.out.println(-1);
            else System.out.println(minLen + " " + maxLen);
        }
    }
}