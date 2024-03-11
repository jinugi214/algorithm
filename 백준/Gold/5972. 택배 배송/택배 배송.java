import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

class Road {
    int num;
    int cows;

    public Road(int num, int cows) {
        this.num = num;
        this.cows = cows;

    }
}

class Node{
    int vertex; // 현재 노드 번호
    int cost; // 현재 노드까지의 최소 비용

    public Node(int vertex, int cost){
        this.vertex = vertex;
        this.cost = cost;
    }
}

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] inputs = br.readLine().split(" ");

        int N = Integer.parseInt(inputs[0]);
        int M = Integer.parseInt(inputs[1]);

        ArrayList<ArrayList<Road>> roadList = new ArrayList<>();

        for(int i = 0; i<N+1; i++){
            roadList.add(new ArrayList<>());
        }


        for(int i = 0; i<M; i++){
            inputs = br.readLine().split(" ");
            int a = Integer.parseInt(inputs[0]);
            int b = Integer.parseInt(inputs[1]);
            int c = Integer.parseInt(inputs[2]);
            roadList.get(a).add(new Road(b, c));
            roadList.get(b).add(new Road(a, c));
        }

        // 길 방문 여부
        boolean[] visited = new boolean[N+1];

        // 최소비용 테이블
        int[] cost = new int[N+1];

        Arrays.fill(cost, Integer.MAX_VALUE);

        cost[1] = 0;

        // 우선순위 큐를 이용하여 현재 최소 비용 기준으로 정렬한다.
        PriorityQueue<Node> pq = new PriorityQueue<>((n1, n2) -> n1.cost - n2.cost);
        pq.add(new Node(1, 0));

        while(!pq.isEmpty()){
            Node curNode = pq.poll();

            // 이미 방문한 곳은 패스
            if(visited[curNode.vertex]){
                continue;
            }

            visited[curNode.vertex] = true;

            // 현재 최소 비용 길의 인접 길 탐색
            for(Road r : roadList.get(curNode.vertex)){
                int newCost = curNode.cost + r.cows;
                if (newCost < cost[r.num]){
                    cost[r.num] = newCost;
                    pq.add(new Node(r.num, newCost));
                }
            }
        }
        System.out.println(cost[N]);
    }
}