import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int ts = sc.nextInt();
        int p = sc.nextInt();
        sc.nextLine();

        Integer[] scores = new Integer[n];
        if (n > 0) {
            for (int i = 0; i < n; i++) {
                scores[i] = sc.nextInt();
            }
        }


        Arrays.sort(scores, Collections.reverseOrder());

        int rank = 1;
        if (n < p){
            for (int i = 0; i < n; i++){
                if (scores[i] > ts){
                    rank++;
                } else {
                    break;
                }
            }
            System.out.println(rank);
        } else if (n == p && scores[n-1] < ts) {
            for (int i = 0; i < n; i++){
                if (scores[i] > ts){
                    rank++;
                } else {
                    break;
                }
            }
            System.out.println(rank);
        } else {
            System.out.println(-1);
        }
    }
}