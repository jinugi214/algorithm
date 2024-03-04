import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {

    static int[][] nums;
    static List<Integer> result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        nums = new int[2][N+1];

        result = new ArrayList<>();

        for(int i = 1; i< N+1; i++){
            nums[0][i] = i;
            int tmp = Integer.parseInt(br.readLine());
            nums[1][i] = tmp;
            if(i == tmp){
                result.add(i);
            }
        }

        for(int i = 1; i < N+1; i++){
            dfs(new ArrayList<>(), i, i,1);
        }

        Collections.sort(result);

        System.out.println(result.size());
        for(int n : result){
            System.out.println(n);
        }
    }

    static void dfs(List<Integer> lst, int cur, int start, int depth){
        lst.add(cur);
        int next = nums[1][cur];
        if (depth > 1 && next == start){
            if(Collections.disjoint(result, lst)){
                result.addAll(lst);
            }
        }

        if(!lst.contains(next)){
            dfs(lst, next, start, depth + 1);
        }
    }
}