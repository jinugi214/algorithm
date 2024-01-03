import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t< T; t++){
            int N = Integer.parseInt(br.readLine());
            int[] rank = new int[N];
            HashMap<Integer, Integer> people = new HashMap<>();

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++){
                int data = Integer.parseInt(st.nextToken());
                people.put(data, people.getOrDefault(data, 0) + 1); // 같은 팀에 선수 인원 추가
                rank[i] = data; // 결승선 통과한 순서대로 데이터 넣기
            }
            int[] fifthIdx = new int[people.size() + 1];
            HashMap<Integer, Integer> score = new HashMap<>();
            HashMap<Integer, Integer> order = new HashMap<>();
            int cur = 1;

            for (int r : rank){
                if(people.get(r) == 6){ // 선수가 6명이면
                    order.put(r, order.getOrDefault(r, 0) + 1); // 팀의 순서 추가

                    if(order.get(r) <= 4){ // 6명인 선수가 있는 팀 중에 상위 4명 계산
                        score.put(r, score.getOrDefault(r, 0) + cur);
                    }

                    if(order.get(r) == 5){ // 5번째 순서이면
                        fifthIdx[r] = cur; //
                    }
                    cur ++; // 점수 증가
                }
            }

            List<Integer> key = new ArrayList<>(score.keySet());
            key.sort((x, y) -> {
                if(score.get(x).equals(score.get(y))){ // 동점이면
                    return fifthIdx[x] - fifthIdx[y]; // 다섯번째 주자 가장 빨리 들어온팀
                } else {
                    return score.get(x) - score.get(y); // 점수 낮은 팀이 우승
                }
            });

            System.out.println(key.get(0));
        }
    }
}