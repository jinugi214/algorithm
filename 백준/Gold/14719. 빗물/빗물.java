import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");

        int H = Integer.parseInt(inputs[0]);
        int W = Integer.parseInt(inputs[1]);

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] block = new int[W];
        for(int i = 0; i < W; i++){
            block[i] = Integer.parseInt(st.nextToken());
        }

        int h = 0; // 현재 기준되는 블록 높이
        int water = 0; // 현재까지 총 물의 양;
        Stack<Integer> stk = new Stack<>();

        for(int i = 0; i< W; i++){
            if(h == 0 && block[i] > 0){
                h = block[i];
            }
            else if (h > 0 && block[i] < h){
                stk.add(block[i]);
            }
            else if (h > 0 && block[i] >= h){
                int tmpH = Math.min(block[i], h);
                while(!stk.isEmpty()){
                    water += (tmpH - stk.pop());
                }
                h = block[i];
            }
        }

        if(!stk.isEmpty()){
            int tmpH = stk.pop();

            while(!stk.isEmpty()){
                int tmp = stk.pop();
                if (tmpH > tmp){
                  water += tmpH - tmp;
                }
                else if (tmpH < tmp){
                    tmpH = tmp;
                }
            }
        }
        System.out.println(water);
    }
}