public class StrStr {
    public static int strStr(String haystack,String needle){
        if(haystack.contains(needle)){
            return haystack.indexOf(needle);

        }else{
            return -1;
        }
    }


    public static void main(String[] args) {
        String haystack = "hello";
        String needle = "e";
        System.out.println(strStr(haystack,needle));
    }
}
