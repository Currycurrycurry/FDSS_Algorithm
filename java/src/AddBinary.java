
import java.util.HashMap;
import java.util.Map;
public class AddBinary {

    public static boolean useHashMap(int[] nums ,int k){
        String abs = "abcda";
        char[] absCh = abs.toCharArray();



        return false;
    }

    public static boolean decode(int[] nums){

        return false;
    }
    public static int fib(int n){
        if(n == 1 || n==2){
            return 1;
        }

        return fib(n-1)+fib(n-2);
    }
    public static int fibdp(int n,int[] memo){
        int result;

        if(memo[n]!=0){
            return memo[n];
        }

        if(n==1 || n==2){
            result = 1;
        }else{
            result = fib(n-2) + fib(n-1);
        }

        memo[n] = result;
        return result;
    }

    public static int fibBottomup(int n){
        int[] bottom_up = new int[n+1];
        bottom_up[0] = 1;
        bottom_up[1] = 1;
        for (int i = 2; i <=n ; i++) {
            bottom_up[i] = bottom_up[i-1]+bottom_up[i-2];
        }
        return bottom_up[n];
    }

    //i the end index of the array
    public static int rec(int[] arr,int total,int i){
        if(total == 0){
            return 1;
        }else if(total<0){
            return 0;
        }else if(i<0){
            return 0;
        }else if(total < arr[i]){
            return rec(arr,total,i-1);
        }else{
            return rec(arr,total-arr[i],i-1) + rec(arr,total,i-1);
        }
    }

    public static int count_sets(int[] arr,int total){
        return rec(arr,total,arr.length-1);
    }
    public static int mainCountSetsdp(int[] arr,int total){
        HashMap<String,Integer> mem = new HashMap<>();
        return countSetsdp(arr,total,arr.length-1,mem);
    }

    public static int countSetsdp(int[] arr,int total,int i,Map<String,Integer> mem){
        int res;
        String key = total+":"+i;
        if(mem.containsKey(key)){
            return mem.get(key);
        }
        if(total == 0){
            return 1;
        }else if(total < 0){
            return 0;
        }else if(i < 0){
            return 0;
        }else if(total < arr[i]){
            res = countSetsdp(arr,total,i-1,mem);
        }else {
            res = countSetsdp(arr,total - arr[i],i-1,mem) +
                    countSetsdp(arr,total,i-1,mem);
        }
        mem.put(key,res);
        return res;
    }

    public static boolean isHoppableMain(int[] nums){

        //return isHoppable(nums,0,nums.length-1);
        int choices = isHoppable(nums,0,nums.length-1);
        if(choices>0){
            return true;
        }else{
            return false;
        }

    }

    public static int isHoppable(int[] nums,int start,int end){
        int res = 0;
        //base case
        if((end-start) ==1){
            if(nums[start]==0 || (nums[end]+nums[start])<=1){
                return 0;
            }else{
               return 1;
            }
        }else {
                if(nums[start]>0){
                    for (int i = 1; i <=nums[start]&& (start+i)<end; i++) {
                        res +=  isHoppable(nums,start+i,end);
                    }
                }else{
                    return 0;
                }
            }
        return res;

    }
    public static int next_step(int current,int[] nums){
        int res = current;
        int nextSum = 0;
        for (int i = 1; i <=nums[current] ; i++) {
            if((current+i)<nums.length) {
                if (nextSum < (nums[current + i] + i)) {
                    res = current + i;
                    nextSum = nums[current + i] + i;
                }
            }else{
                res = current + i;
            }
        }
        return res;
    }

    public static boolean isHoppableGreedy(int[] nums){
        int current = 0;
        while(true){
            if(current >= nums.length){
                return true;
            }
            if(nums[current]==0){
                return false;
            }
            current = next_step(current,nums);
        }
    }

    public static int countUniversalTrees(TreeNode root){
        int res = 0;

        if(root.left == null && root.right == null){
            res++;
        }else if(root.left!=null && root.right!=null){
            if(root.left.val == root.right.val && root.left.val == root.val){
                res++;
            }
        }
        //countUniversalTrees(root)

        return res;
    }



    public static int[][] twoArraySum(int[] arr1,int[] arr2,int target){
        int[][] res = new int[arr1.length][2];
        int track = 0;
        for (int i = 0; i < arr1.length; i++) {

            for (int j = 0; j < arr2.length; j++) {
                if(arr1[i]+arr2[j]==target){
                    res[track][0] = arr1[i];
                    res[track][1] = arr2[j];
                }
            }
        }
        return res;
    }

    public static int kp01(int n,int capacity,int[] w,int[] v){
        int result,tmp1,tmp2;
        int[][] arr = new int[n][capacity];
        if(n == 0 || capacity == 0){
            result = 0;
        }else if(w[n]>capacity){
            result = kp01(n-1,capacity,w,v);
        }else{
            tmp1 = kp01(n-1,capacity,w,v);
            tmp2 = kp01(n-1,capacity-w[n],w,v);
            result = Math.max(tmp1,tmp2);
        }
        arr[n][capacity] = result;
        return result;
    }
    //p = abc n=2
    //q = abc m = 1

    public static int lcs(char[] p,char[] q,int n,int m,int[][] arr){
        int tmp1,tmp2,result = 0;
        if(n ==0 || m ==0){
            result = 0;
        }else if(p[n-1] == q[m-1]){
            result= 1 + lcs(p,q,n-1,m-1,arr);
        }else if(p[n-1]!=q[n-1]){
            tmp1 = lcs(p,q,n-1,m,arr);
            tmp2 = lcs(p,q,n,m-1,arr);
            result = Math.max(tmp1,tmp2);
        }
        return result;
    }


    //1.recursion 2.memoire 3.bottom-up
    public static String addBinary(String a,String b){

//        long aD = Long.parseLong(a,2);
////        long bD =Long.parseLong(b,2);
////        long cD = aD + bD;
////        return Long.toBinaryString(cD);
//高位全补0
        //String cstr = "";

        if(a.equals("0") && b.equals("0")){
            return "0";
        }
        StringBuffer csb = new StringBuffer("");
        int lenA = a.length();
        int lenB = b.length();
        int abs = Math.abs(lenA - lenB);
        String str0 = "";
        for (int i = 0; i <=abs ; i++) {
            str0+="0";
        }
        if(lenA > lenB){
            b = str0 + b;
            a = "0" + a;

        } else {
            a = str0 + a;
            b = "0" + b;
        }
        lenA = a.length();
        lenB = b.length();
        char atmp,btmp;
        int aint,bint,cint,ac = 0;
        for (int i = 0; i <lenA; i++) {
            atmp = a.charAt(lenA-1-i);
            btmp = b.charAt(lenB-1-i);
            aint = atmp - '0';
            bint = btmp - '0';
            cint = aint + bint + ac;
            switch (cint){
                case 0:
                case 1:{
                    ac = 0;
                }break;

                case 2:{
                    ac = 1;
                    cint = 0;

                }break;

                case 3:{
                    ac = 1;
                    cint = 1;

                }break;
            }
            csb.append(cint);
        }
        //int lenC = csb.length();
//        //if(csb.length()>=2) {
//        System.out.println("before : "+csb);
//
//            while (csb.length()>=2 && csb.charAt(csb.length() - 1) == '0') {
//                System.out.println("value:" + csb.charAt(csb.length() - 1));
//                csb.delete(csb.length() - 2, csb.length() - 1);
//                System.out.println("after : "+csb);
//
//            }
        //}
        String res =  csb.reverse().toString();
        if(res.length()>=2) {
            char x = res.charAt(0);
            while (x != '1') {
                res = res.substring(1);
                x = res.charAt(0);
            }
        }


        return res;



    }
    public static void main(String[] args) {
        //System.out.println(addBinary("10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101","110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"));
        //System.out.println(addBinary("0","0"));
        //System.out.println(Math.floor(1.923));
        //int n = 100000000;
        //int[] memo = new int[n+1];
        //System.out.println(fib(n));
        //System.out.println(fibdp(n,memo));
        //System.out.println(fibBottomup(n));
        //int[] nums = {4,2,0,0,1,0};
        //System.out.println(isHoppableMain(nums));
        //System.out.println(isHoppableGreedy(nums));
        String regex = "[0-9a-zA-Z]+";
        String testStr1 = "123322111ABC";
        System.out.println(testStr1.matches(regex));

    }
}
