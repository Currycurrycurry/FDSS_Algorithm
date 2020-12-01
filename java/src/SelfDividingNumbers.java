import java.util.ArrayList;
import java.util.List;

public class SelfDividingNumbers {
    public static List<Integer> selfDividingNumbers(int left, int right){
        List<Integer> res = new ArrayList<>();
        for (int i = left; i <= right ; i++) {
            int num = i;
            while(num >0){
                if((num%10!=0) && (i % (num%10) == 0)){
                    num/=10;
                }else{
                    break;
                }
            }
            if(num==0){
                res.add(i);
            }
        }
        return res;
    }
    public static void main(String[] args) {
        System.out.println(selfDividingNumbers(1,22));

    }
}
