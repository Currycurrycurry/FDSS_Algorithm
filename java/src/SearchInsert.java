public class SearchInsert {
    public static int searchInsert(int[] nums,int target){
        if(target == nums[nums.length-1]){
            return nums.length-1;
        }

        if(target>nums[nums.length-1]){
            return nums.length;
        }

        for (int i = 0; i <nums.length-1 ; i++) {
            if(target == nums[i]){
                return i;
            }
            if(target > nums[i] && target < nums[i+1]){
                return i+1;
            }

        }
        return 0;

    }

    public static void main(String[] args) {
        int[] nums = {1,2,3,4,7};
        int target = 6 ;
        System.out.println(searchInsert(nums,target));

    }
}
