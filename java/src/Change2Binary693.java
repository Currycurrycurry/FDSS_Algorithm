import java.math.*;

public class Change2Binary693 {
    public static int[] change2Binary(int n){
        int num = 1;

        int tmpN = n;
        while((tmpN=tmpN/2)!=1){
            num++;
        }
        System.out.println("num: "+num);

        int[] binaryInt = new int[num+1];
        binaryInt[0] = 1;


        int tmp = n - (int) Math.pow(2,num);
        for (int i = num; i >=1 ; i--) {
            if(tmp>=(int) Math.pow(2,i-1)){
                binaryInt[num-i+1] = 1;
                tmp -=(int) Math.pow(2,i-1);
            }
        }

        return binaryInt;
    }


    public static boolean hasAlternatingBits(int n) {
        int[] binary = change2Binary(n);

        for (int i = 0; i < binary.length ; i++) {
            System.out.println(binary[i]);
        }
        for (int i = 0; i < binary.length - 1 ; i++) {
            if(binary[i]==binary[i+1]){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(hasAlternatingBits(11));

    }
}
