import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int p = sc.nextInt();

        for (int i = 1; i < p+1; i++){
            int t = sc.nextInt();
            Integer arr[] = new Integer[20];
            for (int j = 0; j < 20; j++) {
                arr[j] = sc.nextInt();
            }

            int cnt = 0;

            for (int j = 1; j < 20; j++){
                for(int k = j-1; k >= 0; k--){
                    if(arr[k]>arr[j]){
                        cnt++;
                    }
                }
            }
            System.out.println(t+" "+cnt);
        }
    }
}