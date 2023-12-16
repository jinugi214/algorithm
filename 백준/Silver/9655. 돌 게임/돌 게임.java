import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int rest = n % 4;
        if (rest == 1 || rest == 3){
            System.out.println("SK");
        } else {
            System.out.println("CY");
        }
    }
}