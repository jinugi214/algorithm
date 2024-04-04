import java.util.*;

class Solution {
    public int[][] solution(int[][] nodeinfo) {
        int[][] answer = new int[2][nodeinfo.length];
        Stack<Integer> pre_st = new Stack<>();
        Stack<Integer> post_st = new Stack<>();
        Node[] nodes = new Node[nodeinfo.length];
        int root_idx = 0;
        
        for(int i = 0; i < nodeinfo.length; i++){
            nodes[i] = new Node(i+1, nodeinfo[i][0], nodeinfo[i][1]);
        }
        Arrays.sort(nodes, new Comparator<Node>(){
            public int compare(Node n1, Node n2){
                return n2.y - n1.y;
            }
        });
        
        Node root = nodes[0];
        for(int i = 1; i < nodes.length; i++){
            makeTree(root, nodes[i]);
        }
        
        preOrder(root, pre_st);
        postOrder(root, post_st);
        for(int i = 0; i < nodeinfo.length; i++){
            answer[0][i] = pre_st.get(i);
            answer[1][i] = post_st.get(i);
        }
        return answer;
    }
    
    public void preOrder(Node root, Stack stack){
        stack.add(root.num);
        if(root.l_child != null)
            preOrder(root.l_child, stack);
        if(root.r_child != null)
            preOrder(root.r_child, stack);
    }
    
     public void postOrder(Node root, Stack stack){
        if(root.l_child != null)
            postOrder(root.l_child, stack);
        if(root.r_child != null)
            postOrder(root.r_child, stack);
        stack.add(root.num);
    }
    
    public void makeTree(Node root, Node newNode){
        if(newNode.x > root.x){
            if(root.r_child == null){
                root.r_child = newNode;
            } else {
                makeTree(root.r_child, newNode);
            }
        } else {
            if(root.l_child == null){
                root.l_child = newNode;
            } else {
                makeTree(root.l_child, newNode);
            }
        }
    }
    
    class Node{
        int x, y, num;
        Node l_child, r_child;
        public Node(int num, int x, int y){
            this.num = num;
            this.x = x;
            this.y = y;
        }
    }
}