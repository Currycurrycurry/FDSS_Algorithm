class DSU{
    int[] root;
    int[] rank;
    int size;

    public DSU(int N){
        root = new int[N];
        rank = new int[N];
        for(int i = 0;i < N;i++){
            root[i] = i;
            rank[i] = 1;
        }
        size = N;
    }

    public int find_loop(int x){
        while(x!=root[x]){
            //compress the path
//            root[x] = root[root[x]];
            x = root[x];
        }
        return x;
      
    }

    // public int find_rec(int x){
    //     if(x!=root[x]){
    //         x = find_rec(x);
    //     }
    //     return x;
    // }

    
    public void union(int x,int y){
        int x_root = find_loop(x);
        int y_root = find_loop(y);

        if(rank[x_root]>y_root){
            root[y_root] = x_root;
            rank[x_root] += rank[y_root];
        }else{
            root[x_root] = y_root;
            rank[y_root] += rank[x_root];
        }
        size--;
    }

}

