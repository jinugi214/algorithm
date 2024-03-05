
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static long[] tree;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] input = new int[3];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i<3; i++){
            input[i] = Integer.parseInt(st.nextToken());
        }

        int N = input[0];
        int M = input[1];
        int K = input[2];

        tree = new long[size(N)];

        for(int i = 0; i < N; i++){
            long val = Long.parseLong(br.readLine());
            update(0, N-1, 1, val, i);
        }

        for(int i = 0; i < M+K; i++){
            String[] vals = br.readLine().split(" ");

            int a = Integer.parseInt(vals[0]);
            int b = Integer.parseInt(vals[1]);


            if(a == 1){
                long c = Long.parseLong(vals[2]);
                update(0, N-1, 1, c, b-1);
            }
            if(a == 2){
                int c = Integer.parseInt(vals[2]);
                System.out.println(cal(0, N-1, b-1, c-1, 1));
            }
        }
    }

    // 값 업데이트
    private static void update(int start, int end, int node, long val, int idx){
        if(start == idx && end == idx){
            tree[node] = val;
            return;
        }
        int mid = (start + end) / 2;
        if(idx <= mid){
            update(start, mid, node * 2, val, idx);
        }
        else{
            update(mid+1, end, node * 2 + 1, val, idx);
        }
        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    // 값 찾기
    private static long cal(int start, int end, int left, int right, int node){
        if(left > end || right < start){
            return 0L;
        }

        if(start >= left && end <= right){
            return tree[node];
        }

        int mid = (start + end) / 2;
        return cal(start, mid, left, right, node * 2) + cal(mid+1, end, left, right, node * 2 + 1);
    }

    // 노드의 높이 찾아내기
    private static int size(long n) {
        int h = (int) Math.ceil(Math.log(n) / Math.log(2)) + 1;
        return (int) Math.pow(2,h);
    }
}