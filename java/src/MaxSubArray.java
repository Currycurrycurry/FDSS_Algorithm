//算法导论
public class MaxSubArray {
    //暴力破解法： n2
    public static int maxSubArray1(int[] nums){
        int maxSum = 0,tmpSum;
        for(int i = 0;i<nums.length;i++){
            tmpSum = 0;
            for (int j = i; j <nums.length ; j++) {
                tmpSum+=nums[j];
                if(tmpSum>maxSum){
                    maxSum = tmpSum;
                }
            }
        }
        return maxSum;
    }

    //递归优化法：nlgn
    public static int maxSUbArray2(int[] nums){

        return 0;
    }

    //n
    public static int maxSubArray3(int[] nums){
        int maxSum = 0,tmpSum = 0;
        for (int i = 0; i < nums.length ; i++) {
            tmpSum+=nums[i];
            if(tmpSum>0){
                if(tmpSum>maxSum){
                    maxSum = tmpSum;
                }
            }else{
                tmpSum = 0;
            }
        }
        return maxSum;
    }


    //线性复杂度法：
    public static void main(String[] args) {
        int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
        System.out.println(maxSubArray1(nums));

    }
}
