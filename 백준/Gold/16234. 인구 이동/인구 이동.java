import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Country {
    int r;
    int c;

    public Country(int r, int c) {
        this.r = r;
        this.c = c;
    }

    @Override
    public String toString() {
        return "[" + this.r + ", " + this.c + "]";
    }
}


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");

        int N = Integer.parseInt(inputs[0]);
        int L = Integer.parseInt(inputs[1]);
        int R = Integer.parseInt(inputs[2]);

        int[][] world = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                world[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int days = 0;

        // 인구차이 L명 이상, R명 이하이면 문제있는 나라끼리 국경선 열고 인구 공유
        // 인원 => 국경선이 열려있는 나라의 총 인구수 / 나라 개수 (소수점 버리기)
        int[][] direct = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while (true) {
            List<List<Country>> unionList = new ArrayList<>();
            boolean[][] visited = new boolean[N][N];
            for (int x = 0; x < N; x++) {
                for (int y = 0; y < N; y++) {
                    List<Country> union = new ArrayList<>();
                    ArrayDeque<Country> dq = new ArrayDeque<>();
                    dq.add(new Country(x, y));
                    union.add(new Country(x, y));
                    visited[x][y] = true;
                    while (!dq.isEmpty()) {
                        Country country = dq.poll();
                        for (int i = 0; i < 4; i++) {
                            int nr = country.r + direct[i][0];
                            int nc = country.c + direct[i][1];
                            if (nr >= 0 && nr < N && nc >= 0 && nc < N && !visited[nr][nc]) {
                                if (check(Math.abs(world[nr][nc] - world[country.r][country.c]), L, R)) {
                                    dq.add(new Country(nr, nc));
                                    union.add(new Country(nr, nc));
                                    visited[nr][nc] = true;
                                }
                            }
                        }
                    }
                    if (union.size() > 1) {
                        unionList.add(union);
                    }
                }

            }
            if (unionList.isEmpty()) {
                break;
            }

            for (List<Country> union : unionList) {
                int people = 0;
                for (Country c : union) {
                    people += world[c.r][c.c];
                }
                int movedPeople = people / union.size();
                for (Country c : union) {
                    world[c.r][c.c] = movedPeople;
                }
            }
            days++;
        }
        System.out.println(days);
    }

    static boolean check(int val, int L, int R) {
        return val >= L && val <= R;
    }
}