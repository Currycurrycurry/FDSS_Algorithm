

//逆波兰式
//用栈

import java.util.ArrayList;
import java.util.Stack;

public class ValidBrace {
    //Stack<> formula = new Stack<>();
    //ArrayList<Integer> temp = new ArrayList<>();

    public static boolean isValid(String s){
        //temp.
        //Math.
        Stack<Character> formula = new Stack<Character>();
        //System.out.println(formula.size());
        //System.out.println(formula.empty());
        if(s.equals("")){
            return true;
        }
        if(s.length()%2 == 1){
            return false;
        }
        for (int i = 0; i <s.length() ; i++) {
            char tmp = s.charAt(i);
            if(tmp == '(' || tmp== '[' || tmp == '{'){
                formula.push(tmp);
            }else if(tmp == ')' || tmp == ']' || tmp == '}'){
                if(formula.size()!=0){
                    switch (tmp){
                        case ')': {
                            if (formula.peek() == '(') {
                                formula.pop();
                            } else {
                                return false;
                            }
                        }
                            break;

                        case ']': {
                            if (formula.peek() == '[') {
                                formula.pop();
                            } else {
                                return false;
                            }
                        }
                            break;

                        case '}': {
                            if (formula.peek() == '{') {
                                formula.pop();
                            } else {
                                return false;
                            }
                        }
                            break;

                    }


                }
            }

        }
        return formula.empty();
    }
    public static void main(String[] args) {
        System.out.println(isValid("()()()[]"));
    }
}
