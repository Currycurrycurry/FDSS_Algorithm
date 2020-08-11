package Sort;

import java.math.*;
import java.util.*;
//import java.util.ArrayList;
//import java.util.List;
//import java.util.concurrent.CompletionService;

public class Example {
//    public static void sort(Comparable[] a){
//        List<Integer> list = new ArrayList<>();
//        list.
//
//
//    }
    //compare O(n2) exchange O(n)

    public static void selectionSort(Comparable[] a){
        for(int j = 0;j<a.length;j++){
            int min = j;
            for(int i=j+1;i<a.length;i++){
                if(less(a[i],a[min])){
                    min = i;
                }
            }
            exch(a,j,min);
        }
    }

    //!
    public static void insertionSort(Comparable[] a){
      int N = a.length;
      for(int i = 1;i<a.length;i++){
          for(int j = i;j>=0&&less(a[j],a[j-1]);j--){
              exch(a,j,j-1);
          }
      }
    }

    //访问数组的次数减半
    public static void insertionSort2(Comparable[] a){
        int N = a.length;
        for(int i = 1;i<a.length;i++){
            Comparable t = a[i];
            for(int j=i;j>=0;j--){
                if(less(a[i],a[j])){
                    a[j] = a[j-1];
                }else{
                    a[j] = t;
                }
            }
        }
    }

    //!基于插入排序的希尔排序
    public static void shellSort(Comparable[] a){
        int N = a.length;
        int h = 1;
        while(h<N/3){
            h = 3*h+1;
        }
        while(h>=1) {
            for (int i = h; i < N; i++) {
                for (int j = i; j >= 0 && less(a[j], a[j - 1]); j -= h) {
                    exch(a, j, j - h);
                }
            }
            h/=3;
        }
    }

    //递归排序算法 归并排序

    private static Comparable[] aux;

    public static void mergeSort(Comparable[] a){

        aux = new Comparable[a.length];
        mergeSort(a,0,a.length-1);
    }


    public static void mergeSort(Comparable[] a,int start,int end){
        if(end<=start){
            return;
        }
        int mid = start + (end - start)/2;
        mergeSort(a,start,mid);
        mergeSort(a,mid+1,end);
        merge(a,start,mid,end);
    }

    public static void merge(Comparable[] a,int low,int mid,int high){
        int i=low,j=mid+1;
        for(int k=low;k<=high;k++){
            aux[k] = a[k];
        }
        for(int k = low;k<=high;k++){
            if(i>mid){
                a[k] = aux[j++];
            }else if(j > high){
                a[k] = aux[i++];
            }else if(less(aux[j],aux[i])){
                a[k] = aux[j++];
            }else{
                a[k] = aux[i++];
            }

        }
    }


    public static void quickSort(Comparable[] a){
        quickSort(a,0,a.length-1);
    }


    public static int partition(Comparable[] a,int start,int end){
        int i = start;
        int j = end+1;
        Comparable v = a[start];
        int ran_index = (int)(Math.random() * (end - start + 1));
        Comparable v_ = a[ran_index];

        while(true){

            while(less(a[++i],v)){
                if(i==end){
                    break;
                }
            }

            while(less(v,a[--j])){
                if(j==start){
                    break;
                }
            }

            if(i>=j){
                break;
            }
            exch(a,i,j);
        }
        exch(a,start,j);
        return j;
    }


    public static void quickSort(Comparable[] a,int start,int end){
        if(start>=end){
            return;
        }
        int k = partition(a,start,end);
        quickSort(a,start,k-1);
        quickSort(a,k+1,end);
    }

    public static boolean less(Comparable a,Comparable b){
        return a.compareTo(b) < 0;
    }

    public static void show(Comparable[] a){
        for (Comparable c:a) {
            System.out.print(c+" ");
        }
    }


    public static void exch(Comparable[] a,int i,int j){
        Comparable t = a[i];
        a[i] = a[j];
        a[j] = t;
    }

    public static boolean isSorted(Comparable[] a){
        for(int i=0;i<a.length-1;i++){
            if(less(a[i+1],a[i])){
                return false;
            }
        }
//        if(a==null)
        return true;
    }

    public static int gcd(int p,int q){
        if(q==0){
            return p;
        }
        return gcd(q,p%q);
    }


    public static int gcd2(int p,int q){
        while(q!=0){
            int temp = q;
            q = p%q;
            p = temp;
        }
        return p;
    }


    public static void recursiveDigit(int num){
        int value = num/10;
        if(value!=0){
            recursiveDigit(value);
        }
        System.out.println(num%10);
    }

    public static int region(int[] a,int currentSum,int i){
        currentSum+=a[i];
        System.out.println("out  "+ currentSum) ;          //按顺序输出：递归式前面
        if(i<3){
            region(a,currentSum,i+1) ;
            System.out.println("in  "+ currentSum) ;  //先进后出：递归式后面
        }
        System.out.println("hello  ") ;
        return currentSum ;
    }


    //缺点1：启动大量线程的资源消耗
    //缺点2：数值接近的元素未必按顺序输出
    //缺点3：遇到很大的元素，线程睡眠时间过于长

    public static void sleepSort(int[] array){
        for(int num:array){
            new Thread(()->{
                try{
                    Thread.sleep(num);
                }catch(InterruptedException e){
                    e.printStackTrace();
                }
                System.out.println(num);
            }).start();
        }
    }

    public static void printArray(int[] nums){
        for(int i:nums){
            System.out.print(i+" ");
        }

        System.out.println();
    }

    public static void swap(int[] nums,int i, int j){
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

    public static void permutation(int[] nums,int start){
        if(start == nums.length-1){
            printArray(nums);
        }else{
            int tmp;
            for(int i = start;i <= nums.length-1;i++){
                swap(nums,i,start);
                permutation(nums,start+1);
                swap(nums,i,start);
            }
        }
    }

    public static void permutation(int[] nums){
        if(nums==null){
            return;
        }
        permutation(nums,0);
    }

    public static int combination(int[] nums,int m){

        if(nums == null || nums.length == 0 || nums.length < m || m < 0){
            return 0;
        }
        if(m == 0){
            return 1;
        }
        if(m == 1){
            return nums.length;
        }
        if(nums.length == m){
            return 1;
        }
        return combination(nums,0,m);
    }


    public static int combination(int[] nums,int start,int m){

        if(m == nums.length - 1 - start){
            return 1;
        }

        if(m == 1){
            return nums.length - 1 - start;
        }

        return combination(nums,start + 1, m) + combination(nums,start + 1,m-1);

    }
//    /**
//     * 题目：输入一个字符串，打印出该字符事中字符的所有排列。例如输入字符串abc。
//     * 则打印出由字符a、b、c 所能排列出来的所有字符串abc、acb、bac、bca、cab和cba。
//     *
//     * @param chars 待排序的字符数组
//     */
//    public static void permutation(char[] chars) {
//        // 输入较验
//        if (chars == null || chars.length < 1) {
//            return;
//        }
//
//        // 进行排列操作
//        permutation(chars, 0,0);
//    }
//
//    /**
//     * 求字符数组的排列
//     *
//     * @param chars 待排列的字符串
//     * @param begin 当前处理的位置
//     */
//    public static void permutation(char[] chars, int begin,int count) {
//        // 如果是最后一个元素了，就输出排列结果
//        if (chars.length - 1 == begin) {
//            System.out.print(new String(chars) + " ");
//
//        } else {
//            char tmp;
//            // 对当前还未处理的字符串进行处理，每个字符都可以作为当前处理位置的元素
//            for (int i = begin; i < chars.length; i++) {
//                // 下面是交换元素的位置
//                tmp = chars[begin];
//                chars[begin] = chars[i];
//                chars[i] = tmp;
//
//                // 处理下一个位置
//                permutation(chars, begin + 1,count + 1);
//
//                //
//                tmp = chars[begin];
//                chars[begin] = chars[i];
//                chars[i] = tmp;
//            }
//        }
//    }



    public static void main(String[] args){
//        Integer[] nums = {9,8,7,6,5,4,3,2,1};
//        mergeSort(nums);
//        for(Integer i:nums){
//            System.out.println(i);
//        }
        int[] a = {1,2,3} ;
//        char[] a = {'a','b','c','d'};
//        permutation(a);
        System.out.print(combination(a,2));
//        sleepSort(a);
//        System.out.println("final  "+region(a,0,0)) ;
//        String a = "123";

//        LinkedList<Integer> result = new LinkedList<>();
//        result.addFirst(1);
//        result.addLast(2);
//        result.removeFirst();
//        result.removeLast();
//        result.remove(1);


    }


}
