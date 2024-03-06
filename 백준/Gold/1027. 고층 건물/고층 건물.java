import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] buildingList = new int[N];
        int[] answer = new int[N];

        for (int i = 0; i < N; i++) {
            buildingList[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < N - 1; i++) {
            double maxSlope = -Double.MAX_VALUE;
            for (int j = i + 1; j < N; j++) {
                double slope = (double) (buildingList[j] - buildingList[i]) / (j - i);
                if (slope <= maxSlope) {
                    continue;
                }
                maxSlope = Math.max(maxSlope, slope);
                answer[i]++;
                answer[j]++;
            }
        }

        int max = answer[0];

        for (int i = 1; i < N; i++) {
            if (answer[i] > max) {
                max = answer[i];
            }
        }

        System.out.println(max);
    }
}