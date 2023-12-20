import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        int[][] board = new int[n][4];

        for (int i = 0; i < n; i++){
            int country = sc.nextInt();
            int gold = sc.nextInt();
            int silver = sc.nextInt();
            int bronze = sc.nextInt();
            board[i][0] = country;
            board[i][1] = gold;
            board[i][2] = silver;
            board[i][3] = bronze;
        }

        // board 배열을 0, 1, 2 인덱스를 기준으로 내림차순 정렬
        Arrays.sort(board, (a, b) -> {
            if (a[1] != b[1]) {
                return b[1] - a[1];
            } else if (a[2] != b[2]) {
                return b[2] - a[2];
            } else {
                return b[3] - a[3];
            }
        });

        int[] rank = new int[n+1];

        for (int i = 0 ; i < n; i++){
            if (i > 0 && board[i][1] == board[i-1][1] && board[i][2] == board[i-1][2] && board[i][3] == board[i-1][3]){
                rank[board[i][0]] = rank[board[i-1][0]];
            } else {
                rank[board[i][0]] = i+1;
            }

        }

        System.out.println(rank[k]);
    }

}