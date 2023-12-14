import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        System.out.print(fibonacci(n) + " " + (n - 2));
    }
    public static int fibonacci(int n){
        int cnt = 1;
        int[] f = new int[n+1];

        f[1] = f[2] = 1;
        for(int i = 3; i<n+1; i++){
            f[i] = f[i-1] + f[i-2];
            cnt += 1;
        }

        return f[n];
    }
}