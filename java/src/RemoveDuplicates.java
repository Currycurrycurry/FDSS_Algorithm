
//这是一个排序数组！！！！！
//不使用额外的数组空间，在原地修改输入数组并在使用o(1)的额外空间的条件下完成
public class RemoveDuplicates {

    public static int removeDuplicates(int[] nums){
        //int realLen;
        //nums[0]
        int realEnd = 1;
        for (int i = 1; i <nums.length ; i++) {
            if(nums[i]!=nums[i-1]){
                nums[realEnd] = nums[i];
                realEnd++;
            }
        }

        return realEnd;
    }

    public static void main(String[] args) {

        int[] arr = {0,0,0,0,0,0,1};
        //System.out.println(removeDuplicates(arr));
        int len = removeDuplicates(arr);
        for (int i = 0; i < len ; i++) {
            System.out.println(arr[i]);
        }

    }
}
