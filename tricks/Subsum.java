import java.util.HashMap;

public class Subsum {
    public static int subarraySum(int[] nums, int k) {
        int n = nums.length;
        HashMap<Integer, Integer> preSum = new HashMap<>();
        preSum.put(0, 1);
        int ans = 0, sum0_i = 0;
        for (int i = 0; i < n; i++) {
            sum0_i += nums[i];
            int sum0_j = sum0_i - k;
            if (preSum.containsKey(sum0_j)) {
                ans += preSum.get(sum0_j);
            }
            preSum.put(sum0_i, preSum.getOrDefault(sum0_i, 0) + 1);
        }
        return ans;

    }

    public static int calExamPercentage(int[] scores) {
        int[] count = new int[150 + 1];
        for (int score: scores) {
            count[score] ++;
        }
        for (int i = 1; i < count.length; i++) {
            count[i] += count[i-1];
        }
    }
    
    public static void main(String[] args){
        int[] array = {1,2,1,2};
        System.out.println(subarraySum(array, 3));

    }
}