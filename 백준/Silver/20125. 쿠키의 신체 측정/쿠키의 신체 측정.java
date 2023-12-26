import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        boolean start = false;
        boolean arm = false;
        boolean waist = false;

        int heart = 0; // 심장 위치 x, y
        int[] body = new int[5];

        for (int i = 1; i < n+1; i++){
            String input = sc.nextLine();
            if (!start && input.contains("*")){
                heart = input.indexOf("*");
                start = true;
                System.out.println(i + 1 + " " + (heart + 1));
            } else {
                if (!arm){
                    if (input.charAt(heart) == '*') {
                        int left = 0;
                        int right = 0;

                        for (int j = 0 ; j < heart; j++){
                            if (input.charAt(j) == '*'){
                                left++;
                            }
                        }

                        for (int j = heart + 1; j < n; j++ ) {
                            if (input.charAt(j) == '*'){
                                right++;
                            }
                        }

                        body[0] = left;
                        body[1] = right;
                        arm = true;
                    }
                } else if (input.charAt(heart) == '*') {
                        body[2] += 1;
                } else {
                    if (input.charAt(heart-1) == '*'){
                        body[3] += 1;
                    }
                    if (input.charAt(heart+1) == '*'){
                        body[4] += 1;
                    }
                }

            }
        }

        for (int i = 0; i < 5; i++){
            System.out.print(body[i]);
            if (i != 4){
                System.out.print(" ");
            }
        }
    }
}