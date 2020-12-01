

//给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。
//
//我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。
//说明:  n 的范围为 [1, 10,000]。

import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;

public class NotIncreArr {


    //n-1
    public static boolean checkPossibility(int[] nums) {
        int count = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < nums[i - 1]) {
                count++;
                if (count > 1) {
                    return false;
                }
                int privous = i > 1 ? nums[i - 2] : 0;
                int after = i < nums.length - 1 ? nums[i + 1] : 10000;
                if (nums[i - 1] > after && nums[i] < privous) {
                    return false;
                }
            }
        }
        return true;



    }

    public static void main(String[] args) {
//        Scanner in = new Scanner(System.in);
//        String inputStr = in.nextLine();
//        StringTokenizer stringTokenizer = new StringTokenizer(inputStr," ",false);
//        ArrayList<String> arr = new ArrayList<>();
//        while(stringTokenizer.hasMoreElements()){
//            arr.add(stringTokenizer.nextToken());
//        }
//        
        int[] arr = {4,2,3};
        System.out.println(checkPossibility(arr));
        //checkPossibility(arr);


    }
}