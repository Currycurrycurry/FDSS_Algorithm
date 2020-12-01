//import java.util.Arrays;
//method1: string api no use!!!!
public class RemoveElement {
    public static int removeElement(int[] nums,int val){
        int realEnd = 0;
        for (int i = 0; i <nums.length ; i++) {
            if(nums[i] != val){
                nums[realEnd] = nums[i];
                realEnd++;
            }
        }
        return realEnd;

//        String s = Arrays.toString(nums);
//        String valS = val+"";
//        s.replace(valS,"");
//        nums = s.
    }

    public static void main(String[] args) {

        int[] nums = {1,2,2,2,2,2,2,3,4,3,2,2,2};

        int len = removeElement(nums,2);

        for (int i = 0; i < len ; i++) {
            System.out.println(nums[i]);
        }


    }
}
