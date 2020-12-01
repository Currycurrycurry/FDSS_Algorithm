public class MyPow50 {

    public static double myPow(double x,int n){
        if(n==0){
            return 1.0;
        }
        double tmp = myPow(x,n/2);
        if(Math.abs(n%2)==1){
            return n<0?1/(x*tmp*tmp) : x*tmp*tmp;
        }else{
            return tmp*tmp;
        }


    }


    public static void main(String[] args) {
        System.out.println(myPow(2.0,-3));
        System.out.println(-3/2);

    }
}
