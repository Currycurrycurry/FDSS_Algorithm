public class Palindrome {
    //愚蠢做法
    public static boolean isPalindrome1(int x){
        String xstr = x+"";
        String ystr = new StringBuffer(xstr).reverse().toString();
       return xstr.equals(ystr);
    }
    //神仙做法
    public static boolean isPalindrome2(int x){
        //特殊情况的考虑：负数x 10的倍数x
        if(x<0 || (x%10 == 0&& x!=0)) {
            return false;
        }
        int revertedNumber = 0;
        while(x > revertedNumber){
            //对整数进行翻转
            revertedNumber = revertedNumber*10 + x%10;
            x/=10;
        }

        /*
        r x 1 1232
            12 123
            123 12



         */
        //偶数情况/奇数情况
        return x==revertedNumber || x==revertedNumber/10;
    }
    public static void main(String[] args) {
        System.out.println(isPalindrome2(12321));

    }
}
