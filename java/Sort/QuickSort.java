package Sort;

import java.util.Arrays;
import java.util.Random;

//12:19 12:30 13:01
public class QuickSort {
    private static Random random = new Random();

    public static void normalQuickSort(int[] array, int start, int end) {
        if (start >= end) {
            return;
        }
        int pivot = array[start];
        int left = start;
        int right = end + 1;

        while (left < right) {
            while (array[++left] <= pivot) {
                if (left == end) {
                    break;
                }
            }

            while (array[--right] >= pivot) {
                if (right == start) {
                    break;
                }
            }

            if (left >= right) {
                break;
            }

            swap(array, left, right);
        }

        swap(array, start, right);

        normalQuickSort(array, start, right - 1);
        normalQuickSort(array, right + 1, end);
    }

    public static void randomQuickSort(int[] array, int start, int end) {
        if (start < end) {
            return;
        }
        int left = start;
        int right = end;
        int random_index = (int)(Math.random()*(end - start + 1));
        int pivot = array[random_index];

        while (true) {
            while (array[left++] < pivot) {
                if (left == random_index) {
                    break;
                }
            }

            while (array[--right] > pivot) {
                if (right == random_index) {
                    break;
                }
            }

            if (left >= right) {
                break;
            }

            swap(array, left, right);
        }

        swap (array, random_index, right);

        randomQuickSort(array, start, right - 1);
        randomQuickSort(array, right + 1, end);
    }


    public static void normalQuickSort(int[] array) {
        normalQuickSort(array, 0, array.length - 1);

    }

    public static void threeQuickSort(int[] array,int mid) {

        int lowPointer = 0;
        int highPointer = array.length - 1;
        int i = 0;
        while (i <= highPointer) {
            if (array[i] == mid) {
                i++;
            } else if (array[i] < mid) {
                swap(array, i, lowPointer);
                i++;
            } else {
                swap(array, i, highPointer);
            }
        }
    }

    public static void insertionSort(int[] array, int start, int end) {
        for (int i = start + 1; i <= end ; i++) {
            int j = i;
            int val = array[i];
            while (val < array[j]) {
                array[j+1] = array[j];
                j--;
                if (j == 0) {
                    break;
                }
            }
            array[j] = val;
        }
    }

    public static void improvedQuickSort(int[] array, int start, int end) {
        if (end - start <= 15) {
            insertionSort(array, start, end);
            return;
        }
        normalQuickSort(array, start, end);
    }

    public static void improvedQuickSort(int[] array) {
        // k = 10
        improvedQuickSort(array, 0, array.length - 1);

    }

    public static void swap(int[] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    public static void shuffle(int[] array) {
        for (int i = array.length; i >= 0; i--) {
            int rand_index = random.nextInt(i);
            swap(array, i, rand_index);
        }
    }

    public static void print(int[] array) {
        for (int i: array) {
            System.out.print(i + " ");
        }
        System.out.println();
    }


    public static void main(String[] args) {

        int[] array = new int[10];
        for (int i = 0; i < array.length; i++) {
            array[i] = i;
        }
        print(array);
        shuffle(array);
        print(array);
        normalQuickSort(array);
        print(array);

//
//        improvedQuickSort(array);
//        threeQuickSort(array);



    }
}
