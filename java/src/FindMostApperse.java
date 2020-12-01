import java.util.*;

public class FindMostApperse {
    public static List<Integer> getModalNums(int[] arr){
        int n = arr.length;
        if(n == 0){
            return Collections.EMPTY_LIST;
        }
        if(n == 1){
            return Arrays.asList(arr[0]);
        }
        Map<Integer,Integer> freqMap = new HashMap<>();
        for (int i = 0; i < n  ; i++) {
            Integer v = freqMap.get(arr[i]);
            freqMap.put(arr[i],v==null?1:v+1);
        }
        return Collections.EMPTY_LIST;
//
//        List<Map.Entry<Integer,Integer>> entries = new ArrayList<>(freqMap.entrySet());

    }

    public static void main(String[] args) {
        System.out.println(1/2);

    }

}
