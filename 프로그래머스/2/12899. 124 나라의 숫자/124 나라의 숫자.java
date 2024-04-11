class Solution {
    public String solution(int n) {
        
        // 124 나라에서는 0이 존재하지 않고,
        // 3으로 나누었을 때 나머지가 0인 경우를 4로 치환하기 위해
        // 0번 인덱스에 "4"를 넣는다.
        String[] num = {"4", "1", "2"}; 
        String answer = "";
        
        while(n > 0){
            answer = num[n % 3] + answer;
            n = (n - 1) / 3; // 3으로 나누어떨어지는 경우 4로 표현하기 위해
        }
        return answer;
    }
}