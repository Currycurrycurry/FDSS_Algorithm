public class Roman2Int {
    public static int romanToInt(String s){
        int result = 0;
        int I=1,V=5,X=10,L=50,C=100,D=500,M=1000;
        int IV=4,IX=9;
        int XL=40,XC=90;
        int CD=400,CM=900;
        for (int i = 0; i <s.length() ; i++) {
            switch (s.charAt(i)){
                //!
                case 'I':{
                    if(i<s.length()-1){
                    switch (s.charAt(i+1)){
                        case 'V':result+=IV;i++;break;
                        case 'X':result+=IX;i++;break;
                        default:result+=I;break;
                    }}else{
                        result+=I;
                    }

                }break;
                case 'V':result+=V;break;
                //!
                case 'X':{
                    if(i<s.length()-1){
                    switch (s.charAt(i+1)) {
                        case 'L':
                            result += XL;
                            i++;
                            break;
                        case 'C':
                            result += XC;
                            i++;
                            break;
                        default:result+=X;
                            break;
                    }
                    }else{
                        result+=X;
                    }
                }break;
                case 'L':result+=L;break;
                //!
                case 'C':{
                    if(i<s.length()-1) {
                        switch (s.charAt(i + 1)) {
                            case 'D':
                                result += CD;
                                i++;
                                break;
                            case 'M':
                                result += CM;
                                i++;
                                break;
                            default:
                                result += C;
                                break;
                        }
                    }else{
                        result+=C;
                    }
                }break;
                case 'D':result+=D;break;
                case 'M':result+=M;break;
                default:break;

            }

        }

        return result;
    }
    public static void main(String[] args) {
        System.out.println(romanToInt("MCMXCIV"));
    }
}
