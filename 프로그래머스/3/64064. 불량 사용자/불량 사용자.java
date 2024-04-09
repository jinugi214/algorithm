import java.util.*;

class Solution {
    
    String[] userIds;
    String[] bannedIds;
    boolean[] visited;
    HashSet<HashSet<String>> result = new HashSet<>();
    
    public int solution(String[] user_id, String[] banned_id) {
        userIds = user_id;
        bannedIds = banned_id;
        visited = new boolean[user_id.length];
        
        dfs(new HashSet<>(), 0);
        
        return result.size();
    }
    
    void dfs(HashSet<String> set, int depth){
        if (depth == bannedIds.length){
            result.add(set); // 경우가 겹치지 않게 새로운 경우를 추가
            return;
        }
        
        for (int i = 0; i < userIds.length; i++){
            if (set.contains(userIds[i])) {
                continue; // 이미 포함된 제재 아이디면 패스
            }
            
            if(check(userIds[i], bannedIds[depth])){
                set.add(userIds[i]); // 제재 아이디가 맞다면
                dfs(new HashSet<>(set), depth + 1);
                set.remove(userIds[i]);
            }
        }
    }
    
    boolean check(String userId, String bannedId){
        if (userId.length() != bannedId.length()){
            return false; // 길이 안맞으면
        }
        
        boolean tf = true;
        for(int i = 0; i < userId.length(); i++){
            if(bannedId.charAt(i) != '*' && userId.charAt(i) != bannedId.charAt(i)){
                tf = false; // 서로 글자가 안맞으면
                break;
            }    
        }
        return tf;
    }
    
}