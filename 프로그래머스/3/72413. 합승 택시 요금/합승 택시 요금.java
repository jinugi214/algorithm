import java.util.*;

class Edge implements Comparable<Edge> {
    int index;
    int cost;

    Edge(int index, int cost) {
        this.index = index;
        this.cost = cost;
    }

    @Override
    public int compareTo(Edge o) {
        return 0;
    }
}

class Solution {
    static final int INF = 200 * 100000 + 1;
    static List<List<Edge>> graph = new ArrayList<>();

    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = INF;

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] i : fares) {
            graph.get(i[0]).add(new Edge(i[1], i[2]));
            graph.get(i[1]).add(new Edge(i[0], i[2]));
        }

        int[] startA = new int[n + 1];
        int[] startB = new int[n + 1];
        int[] start = new int[n + 1];

        Arrays.fill(startA, INF);
        Arrays.fill(startB, INF);
        Arrays.fill(start, INF);

        startA = dijkstra(a, startA);
        startB = dijkstra(b, startB);
        start = dijkstra(s, start);

        for(int i=1;i<=n;i++) {
            answer = Math.min(answer, startA[i]+startB[i]+start[i]);
        }
        return answer;
    }

    public int[] dijkstra(int start, int[] costs) {
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        pq.offer(new Edge(start, 0));
        costs[start] = 0;

        while (!pq.isEmpty()) {
            Edge now = pq.poll();
            int nIndex = now.index;
            int nCost = now.cost;

            if (nCost > costs[nIndex]) {
                continue;
            }

            List<Edge> edges = graph.get(nIndex);
            for (Edge e : edges) {
                int cost = e.cost + costs[nIndex];

                if (cost < costs[e.index]) {
                    costs[e.index] = cost;
                    pq.offer(new Edge(e.index, cost));
                }
            }
        }
        return costs;
    }
}