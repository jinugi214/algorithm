import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        List<String> wordList = new ArrayList<>();

        for(int i = 0; i<N; i++){
            String input = br.readLine();
            if(!wordList.contains(input)) wordList.add(input); // 중복입력 방지
        }

        String S = "";
        String T = "";
        int maxLen = 0;

        for(int i = 0; i<N; i++){
            String standard = wordList.get(i);
            for(int j = i + 1; j<N; j++){
                String comparison = wordList.get(j);
                int len = check(standard, comparison);
                if(len > maxLen){
                    S = standard;
                    T = comparison;
                    maxLen = len;
                }
            }
        }

        System.out.println(S);
        System.out.println(T);


    }
    static int check(String a, String b){
        int lmt = Math.min(a.length(), b.length());
        int cnt = 0;
        for(int i = 0; i<lmt; i++){
            if(a.charAt(i) == b.charAt(i)){
                cnt++;
            } else {
                break;
            }
        }
        return cnt;
    }
}