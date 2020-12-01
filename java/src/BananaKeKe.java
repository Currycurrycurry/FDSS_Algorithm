public class BananaKeKe {
    public int max(int[] piles){
        int max = 0;
        for(int i = 0;i<piles.length;i++){
            if(piles[i]>max){
                max = piles[i];
            }

        }
        return max;
    }
    public int sum(int[] piles){
        int sum = 0;
        for(int i = 0;i<piles.length;i++){
            sum+=piles[i];
        }
        return sum;
    }
    public int minEatingSpeed(int[] piles, int H) {

        int start = 0;
        if(H == piles.length){
            return max(piles);
        }
        if(H > piles.length){
            start = sum(piles)/H;

            while(true){
                int time = 0;
                for(int i = 0;i<piles.length;i++){
                    //System.out.println(Math.ceil(piles[i]/start));
                    double temp = piles[i]/(double)start;
                    //System.out.println(temp);
                    time+= Math.ceil(temp);
                    //System.out.println(time);
                }
                if(time>H){
                    start++;
                }else{
                    break;
                }
            }

        }
        return start;

    }
}
