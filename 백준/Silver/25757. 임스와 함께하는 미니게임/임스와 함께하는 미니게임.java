import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();
        String[] tmp = input.split(" ");
        int n = Integer.parseInt(tmp[0]);
        String game = tmp[1];
        Set<String> set = new HashSet<String>();

        int lmt = 0;
        switch (game) {
            case "Y":
                lmt = 2;
                break;
            case "F":
                lmt = 3;
                break;
            case "O":
                lmt = 4;
                break;
        }

        int cnt = 1; // 본인 포함
        int ans = 0;
        for (int i = 0; i < n; i++){
            String name = sc.nextLine();
            if (!set.contains(name)){
                cnt++;
                set.add(name);
            }

            if (cnt == lmt){
                ans++;
                cnt = 1;
            }
        }
        System.out.println(ans);
    }
}