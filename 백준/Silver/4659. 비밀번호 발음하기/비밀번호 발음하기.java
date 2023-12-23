import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        List<Character> vowels = Arrays.asList('a', 'e', 'i', 'o', 'u');

        Scanner sc = new Scanner(System.in);

        while (true){

            String pwd = sc.next();

            if (pwd.equals("end")) {
                break;
            } else {
                boolean completed = true;
                boolean cdn = false;
                int mo = 0;
                int ja = 0;
                char prev = 0;
                for (char ch : pwd.toCharArray()) {
                    if (vowels.contains(ch)){
                        cdn = true;
                        mo += 1;
                        ja = 0;
                    } else {
                        ja += 1;
                        mo = 0;
                    }
                    if (mo >= 3 || ja >= 3){
                        System.out.println("<" + pwd + "> is not acceptable.");
                        completed = false;
                        break;
                    } else if (prev == ch && ch != 'e' && ch != 'o') {
                        System.out.println("<" + pwd + "> is not acceptable.");
                        completed = false;
                        break;
                    } else {
                        prev = ch;
                    }
                }
                if (completed) {
                    if (!cdn){
                        System.out.println("<" + pwd + "> is not acceptable.");
                    } else {
                        System.out.println("<" + pwd + "> is acceptable.");
                    }
                }

            }
        }
    }
}