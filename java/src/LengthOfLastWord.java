public class LengthOfLastWord {
    public static int lengthOfLastWord(String s){
        String[] tmp = s.split(" ");
        int len = tmp.length;
        if(len>=1) {
            return tmp[len-1].length();
        }else{
            return 0;
        }
    }
    public static void main(String[] args) {
        //String s = " ".split(" ")[0];
        //System.out.println(s);
        System.out.println(lengthOfLastWord(" "));


    }
}
