import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;
public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] building = new int[N+1];
        int[] cnt = new int[N+1]; // 볼 수 있는 건물 개수
        int[] nearNum = new int[N+1]; // 가장 가까운 건물 번호

        ArrayDeque<Integer> ad;

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 1; i <= N; i++){
            building[i] = Integer.parseInt(st.nextToken());
            nearNum[i] = -100000;
        }

        // 왼쪽에서 오른쪽 순회하면서 건물 확인

        ad = new ArrayDeque<>();
        for(int i=1; i<=N; i++){
            while(!ad.isEmpty() && building[ad.peek()] <= building[i]){
                // 현재 건물의 높이가 스택의 top에 있는 건물의 높이보다 크거나 같다면,
                // 스택에서 건물을 제거 -> 스택에는 현재 건물에서 볼 수 있는 건물들만 남게 된다.
                ad.pop(); // 자신보다 작은 값은 모두 pop
            }
            cnt[i] = ad.size(); // 왼쪽에서 오른쪽으로 볼 수 있는 건물 수
            if(cnt[i] > 0) nearNum[i] = ad.peek();
            ad.push(i);
        }

        // 오른쪽에서 왼쪽 순회하면서 건물 확인
        ad = new ArrayDeque<>();
        for(int i=N; i>0; i--){
            while(!ad.isEmpty() && building[ad.peek()] <= building[i]){
                ad.pop();
            }
            int s = ad.size();
            cnt[i] += s; // 오른쪽에서 왼쪽으로 볼 수 있는 건물 수 더해주기
            // 왼쪽에서 볼 수 있는 건물과 오른쪽에서 볼 수 있는 건물 중 더 가까운 건물을 선택
            if(s > 0 && ad.peek()-i < i-nearNum[i]) nearNum[i] = ad.peek();
            ad.push(i);
        }

        StringBuilder sb = new StringBuilder();
        for(int i=1; i <= N; i++){
            sb.append(cnt[i]);
            if(cnt[i] > 0){
                sb.append(" ").append(nearNum[i]);
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}