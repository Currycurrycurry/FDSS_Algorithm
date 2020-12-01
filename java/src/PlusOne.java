//！！！！！！
public class PlusOne {

    public static int[] plusOne(int[] digits){

//        String s = "";
//        for (int i = 0; i <digits.length ; i++) {
//          s+=digits[i];
//        }
//
//       Long tmpInt = Long.parseLong(s) + 1;
//
//        s = tmpInt+"";
//        int[] result = new int[s.length()];
//        for (int i = 0; i <s.length() ; i++) {
//            result[i] = s.charAt(i) - '0';
//        }
//
//        return result;

        //case 1 : normal

        //case 2:进位
        if(digits.length == 0) return null;

        int index = digits.length -1;
        while(digits[index] == 9){
            if(index == 0){
                int[] res = new int [digits.length+1];
                //10,100,1000,10000,100000...
                res[0]=1;
                for (int i = 1; i <res.length ; i++) {
                    res[i] = 0;
                }
                return res;
            }
            digits[index] = 0;
            index --;

        }
        digits[index] +=1;
        return digits;


    }

    public static int[] addOne(int[] nums){
        int sum = 0;
        int carry = 1;
        int[] result = new int[nums.length];
        for (int i = nums.length-1; i >=0 ; i--) {
            sum = nums[i] + carry;
            if(sum == 10)
                carry = 1;
            else
                carry = 0;
            result[i] = sum % 10;
        }
        if(carry == 1){
            result = new int[nums.length+1];
            result[0] = 1;
        }
        return result;
    }
    public static void main(String[] args) {
        int[] digits = {9,8,7,6,5,4,3,2,1,0,9,9,9,9,9,9,9};
        int[] result = plusOne(digits);
        for (int i = 0; i <result.length ; i++) {
            System.out.println(result[i]);
        }

    }
}
