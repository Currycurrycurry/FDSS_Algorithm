public class MergeArrs {
    public static void merge(int[] nums1,int m,int[] nums2,int n){

        int[] nums = new int[m+n];
        int i = 0;
        int head1 = 0;
        int head2 = 0;
        while(i<m+n){
            if((head1<m && head2<n ) && nums1[head1]<nums2[head2]){
                nums[i] = nums1[head1];
                head1++;

            } else if(head1<m && head2<n){
                nums[i] = nums2[head2];
                head2++;
            }

            //加if-else补充判断 当前面一组已经便利完之后，直接加上后面一组剩余的数字
            i++;
        }

        i = head1 +head2;
        if(head1==m && head2 < n ){
            while(head2<n){
                nums[i] = nums2[head2];
                i++;
                head2++;

            }
        }

        if(head2 == n && head1 < m){
            while(head1<m){
                nums[i] = nums1[head1];
                i++;
                head1++;
            }
        }


        //nums1 = nums;
        for (int j = 0; j <m+n ; j++) {
            nums1[j] = nums[j];
        }

    }
    public static void main(String[] args) {
        int[] nums1 = {1,2,3,0,0,0,0,0,0,0,0};
        int[] nums2 = {2,3,3,3,4,4,5,6,};
        int m = 3;
        int n = 8;
        merge(nums1,m,nums2,n);
        for (int i = 0; i <nums1.length ; i++) {
            System.out.println(nums1[i]);
        }




    }
}
