import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class t2 {
    static class Node{
        List<Node> children = new ArrayList<>();
        int inDegree;
        boolean reached;
        int count;
    }
    static Node[] nodes ;
    static  int[] father;
    static int n;
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        n = input.nextInt();
        int m = input.nextInt();
        nodes = new Node[n];
        father = new int[n];
        for (int i = 0 ; i < n; i++){
            nodes[i] = new Node();
            father[i] = i;
        }
        input.nextLine();
        String[] s = new String[m];
        for (int i = 0 ; i < m; i++){
            s[i] = input.nextLine();
            String[] temp = s[i].split(" ");
            int temp1 = Integer.parseInt(temp[0]);
            String com = temp[1];
            int temp2 = Integer.parseInt(temp[2]);
            if (com.compareTo("=") == 0){
                union(temp1, temp2);
            }
        }
        for (int i = 0 ; i < n; i++){
            int fa = getFather(i);
            nodes[fa].count++;
            nodes[i] = nodes[fa];
        }

        for (int i = 0; i < m; i++){
            String[] temp = s[i].split(" ");
            int temp1 = Integer.parseInt(temp[0]);
            String com = temp[1];
            int temp2 = Integer.parseInt(temp[2]);
            if (com.compareTo("<") == 0){
                nodes[temp1].children.add(nodes[temp2]);
                nodes[temp2].inDegree++;
            }
            if (com.compareTo(">") == 0){
                nodes[temp2].children.add(nodes[temp1]);
                nodes[temp1].inDegree++;
            }
        }
        Node root = null;
        for (int i = 0 ; i < n; i++){
            if (nodes[i].inDegree == 0)
                root = nodes[i];
        }
        if (root == null){
            System.out.println("信息包含冲突");
            return;
        }
        search(root);
        if (isCircle){
            System.out.println("信息包含冲突");
            return;
        }
        if (flag){
            System.out.println("能确定");
        }else {
            System.out.println("信息不完全");
        }
    }
    public static void union(int x, int y){
        int fx = father[x];
        int fy = father[y];
        if (fx != fy){
            father[fx] = fy;
        }
    }
    public static int getFather(int x){
        if (father[x] == x)
            return x;
        else {
            father[x] = getFather(father[x]);
            return father[x];
        }
    }
    static int reachNode = 0;
    static boolean isCircle = false;
    static boolean flag = false;
    public static void search(Node node){
        node.reached = true;
        reachNode = reachNode + node.count;
        if (reachNode == n){
            flag = true;
        }
        if (isCircle){
            return;
        }
        int size = node.children.size();
        for (int i = 0 ; i < size; i++){
            Node child = node.children.get(i);
            if (!child.reached){
                search(child);
            }else {
                isCircle = true;
                flag = false;
            }
        }
        reachNode = reachNode - node.count;
        node.reached = false;
    }
}