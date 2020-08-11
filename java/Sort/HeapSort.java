package Sort;

import java.util.Scanner;

public class HeapSort {

    public static void swap(int[] array, int i, int j) {
        int tmp = array[i];
        array[i] = array[j];
        array[j] = tmp;
    }

    public static void maxHeapify(int[] array, int size, int i) {
        int j = 2 * i + 1;
        while (j < size) {
            if ((j + 1) < size && array[j + 1] > array[j]) {
                j++;
            }
            if (array[i] >= array[j]) {
                break;
            } else {
                swap(array, i, j);
                i = j;
                j = 2 * j + 1;
            }
        }
    }

    public static void heapSort(int[] array) {
        int size = array.length;
        for (int k = (size - 1) / 2; k >= 0; k++) {
            maxHeapify(array, size, k);
        }
        for (int k = size - 1; k >= 1; k++) {
            swap(array, 0, k);
            maxHeapify(array, k, 0);
        }

    }

    // 二叉堆 堆有序的完全二叉树
    static int[] nums = {6, 5, 4, 3, 2, 1};

    static int size = nums.length;

    static int parent(int i) {
        return (i - 1) / 2;
    }

    static int left(int i) {
        return 2 * i + 1;
    }

    static int right(int i) {
        return 2 * i + 2;
    }

    static void swap(int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    static void maxHeapify(int i) {

        int largest = i;

        if (left(i) >= size) {
            return;
        } else if (nums[i] < nums[left(i)]) {
            largest = left(i);
        }

        if (right(i) >= size) {
            return;
        } else if (nums[i] < nums[right(i)]) {
            largest = right(i);
        }
        if (i != largest) {
            swap(largest, i);
        }
        maxHeapify(largest);

    }

    static void maxHeapify_rc(int i) {
        int j = 2 * i + 1;
        if (j < size) {
            if (j + 1 < size && nums[j + 1] > nums[j]) {
                j++;
            }
            if (nums[i] >= nums[j]) {
                return;
            }
            swap(i, j);
            maxHeapify_rc(j);
        }
    }

    //sink
    static void maxHeapify_loop(int i) {
        int j = 2 * i + 1;
        int temp = 0;
        while (j < size) {
            if (j + 1 < size && nums[j + 1] > nums[j]) {
                j++;
            }
            if (nums[i] >= nums[j]) {
                break;
            }
            temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;

            i = j;
            j = 2 * i + 1;

        }
    }

    static void buildMaxHeap() {
        for (int i = (size - 1) / 2; i >= 0; i--) {
//            maxHeapify(i);
//            maxHeapify_loop(i);
            maxHeapify_rc(i);
        }
    }

    static void printHeap() {
        int k = 0;
        int j = 0;
//        double p = Math.pow(2,j);
        for (int i = size; i >= 0; i -= Math.pow(2, j)) {
            int p = (int) Math.pow(2, j);
            while (p > 0) {
                System.out.print(nums[k]);
                k++;
                if (k >= size) {
                    break;
                }
                p--;
            }
            System.out.println();
            j++;
        }
    }

    static void heapSort() {
        buildMaxHeap();
        printHeap();
        for (int i = size - 1; i > 0; i--) {
            swap(0, i);
            size--;
            maxHeapify_rc(0);
        }
    }

    static void printArray() {
        for (int a : nums) {
            System.out.print(a + " ");

        }
    }

    public static void main(String[] args) {
////        buildMaxHeap();
//        heapSort();
//        System.out.println("after heap sort");
////        printHeap();
//        printArray();
//
//        int[] nums = {5,4,3,2,1};
//        heapSort(nums);
        Scanner in = new Scanner(System.in);
        int userNum = Integer.parseInt(in.nextLine());
        String input_str = in.nextLine();
        String[] rates_str = input_str.split("\\s+");
        int[] rates = new int[userNum];
        for (int i = 0; i < userNum; i++) {
            rates[i] = Integer.parseInt(rates_str[i]);
        }
        int queryNum = Integer.parseInt(in.nextLine());

        String[] queryStr;
        int[] result = new int[queryNum];
        for (int i = 0; i < queryNum; i++) {
            queryStr = in.nextLine().split(" ");
            int left = Integer.parseInt(queryStr[0]);
            int right = Integer.parseInt(queryStr[1]);
            int k = Integer.parseInt(queryStr[2]);
            int tmp = 0;
            for (int j = left - 1; j <= right - 1; j++) {
                if (rates[j] == k) {
                    tmp++;
                }
            }
           result[i] = tmp;
        }

        for (int i = 0; i < queryNum ; i++) {
            System.out.println(result[i]);

        }
    }
}
