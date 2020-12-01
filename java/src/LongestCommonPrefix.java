


public class LongestCommonPrefix {
    public static String longestCommonPrefix(String[] strs){
        if(strs.length == 0){
            return "";
        }
        if(strs.length == 1){
            return strs[0];
        }


        int minLen = 10000;
        String[] tmps = new String[10000];
        boolean tmp = false;
        for (int i = 0; i < strs.length ; i++) {
            if(strs[i].equals("")){
                return "";
            }
            if(minLen>strs[i].length()){
                minLen = strs[i].length();
            }
        }
        loop:
        for (int i = minLen; i >= 0 ; i--) {

            for (int j = 0; j <strs.length ; j++) {
                tmps[j] = strs[j].substring(0,i);
            }

            for (int j = 0; j < strs.length-1 ; j++) {
                if(tmps[j].equals(tmps[j+1])){
                    tmp = true;
                }else{
                    tmp = false;
                    continue loop;

                }
            }

            if(tmp){
                return tmps[0];
            }

        }

        return "";
    }
    public static void main(String[] args) {
        String[] strs = {"abc","abcccc","abccc"};
        //System.out.println(strs[0].substring(0,2));
        System.out.println(longestCommonPrefix(strs));

    }
}
