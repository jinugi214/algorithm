import java.util.HashMap;

class Solution {
    public int[] solution(int[][] edges) {
        int[] answer = new int[4];
        HashMap<Integer, int[]> map = new HashMap<>();

        for (int[] edge : edges) {
            int a = edge[0];
            int b = edge[1];

            if (!map.containsKey(a)) {
                map.put(a, new int[] {0, 0});
            }
            if (!map.containsKey(b)) {
                map.put(b, new int[] {0, 0});
            }
            
            map.get(a)[0]++;
            map.get(b)[1]++;
        }

        for (Integer key : map.keySet()) {
            int[] line = map.get(key);
            
            // 나가는 간선이 2이상이고 들어오는 간선이 0이면 정점
            if (line[0] >= 2 && line[1] == 0) {
                answer[0] = key;
            // 나가는 간선 없이 들어오는 간선이 1개 이상이면 막대
            } else if (line[0] == 0 && line[1] > 0) {
                answer[2]++;
            // 나가는 간선과 들어오는 간선이 모두 2개 이상이면 8자
            } else if (line[0] >= 2 && line[1] >= 2) {
                answer[3]++;
            }
        }
        
        // 나머지는 도넛
        answer[1] = (map.get(answer[0])[0] - answer[2] - answer[3]);

        return answer;
    }
}
