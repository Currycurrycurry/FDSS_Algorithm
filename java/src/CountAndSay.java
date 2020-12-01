
//自动生成报数数列的数组
public class CountAndSay {
    public static String countAndSay(int n){
        String[] strs = new String[30];
        strs[0] = "1";
        strs[1]="11";
        //strs[2]="21";
        for (int i = 2; i <strs.length ; i++) {
            strs[i] = "";
            int time = 1;
            char tmp2;
            //System.out.println(strs[i-1]);
            //char headch = strs[i-1].charAt(0);
            for (int j = 1; j <strs[i-1].length() ; j++) {
                char pre = strs[i-1].charAt(j-1);
                char tmp = strs[i-1].charAt(j);
                if(pre == tmp){
                    time++;
                    if(j == strs[i-1].length()-1){
                        strs[i]+=time;
                        strs[i]+=pre;
                    }
                }else{
                    strs[i]+=time;
                    strs[i]+=pre;
                    time = 1;
                    if(j == strs[i-1].length()-1){
                        strs[i]+=time;
                        strs[i]+=tmp;
                    }
                }


            }

        }

        return strs[n-1];
    }
    public static void main(String[] args) {
        for (int i = 1; i <30 ; i++) {
            System.out.println(countAndSay(i));
        }


    }
}
