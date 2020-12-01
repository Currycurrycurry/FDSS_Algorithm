public class ZhihuExercises {

    public static void zocodc(int[] nums){

        int[] output = new int[nums.length];

        //brute force O(n^2)
        for (int i = 0; i < nums.length ; i++) {
            output[i] = 1;
            for(int j = 0;j<nums.length;j++){
                if(j!=i){
                    output[i]*=nums[j];
                }
            }
        }

        // no zero in the array:  O(N)
        int multiply = 1;
        for (int i = 0; i <nums.length ; i++) {
            multiply *=nums[i];
        }
        for (int i = 0; i <nums.length; i++) {
            output[i] = multiply/nums[i];
        }

        // no division  增加了空间复杂度
        //累乘

        int[] leftArr = new int[nums.length];
        leftArr[0] = nums[0];
        int[] rightArr = new int[nums.length];
        rightArr[nums.length-1] = nums[nums.length-1];

        for (int i = 1; i <nums.length ; i++) {
            leftArr[i] = leftArr[i-1]*nums[i];
        }

        for (int i = nums.length-2; i >=0 ; i--) {
            rightArr[i] = rightArr[i+1]*nums[i];
        }

        for (int i = 0; i <nums.length ; i++) {
            output[i] = leftArr[i-1]*rightArr[i+1];
        }

    }
    public static void main(String[] args) {

    }
}
