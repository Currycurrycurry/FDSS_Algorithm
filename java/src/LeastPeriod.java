public class LeastPeriod {

    public static int bubbleSort(int[] nums){
        int tmp = 0;
        for (int i = 0; i < nums.length ; i++) {
            for (int j = i; j < nums.length; j++) {
                if(nums[i]>nums[j]){
                    tmp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = tmp;
                }

            }

        }

        return 0;

    }

    public static  int calLeast(int[] periods){
        int res = 0;


        return res;
    }



    public static void main(String[] args) {



    }
}
