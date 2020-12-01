public class ReverseInt {
    public static int reverse(int x){
        int result = 0;
        int absX = x>=0?x:-x;
        if(x == -2147483648){
            return 0;
        }
        System.out.print(absX);
        String xstr = absX+"";
        String newStr = new StringBuffer(xstr).reverse().toString();
        double test = Double.valueOf(newStr);
        if(test>=Integer.MIN_VALUE && test<= Integer.MAX_VALUE) {
            result = Integer.valueOf(newStr);
            result = (x > 0) ? result : -result;
        }
        return result;

    }

    public static void main(String[] args) {
        System.out.println(reverse(-2147483648));
        //System.out.println(-2147483648>=0);


    }
}
