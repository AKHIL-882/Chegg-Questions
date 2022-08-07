
// // Java program to evaluate value of a postfix expression
  
// import java.util.Stack;
// import java.util.*;

  
// public class Main 
// {
//     // Method to evaluate value of a postfix expression
//     static int evaluatePostfix(String exp)
//     {
//         //create a stack
//         Stack<Integer> stack=new Stack<>();
          
//         // Scan all characters one by one
//         for(int i=0;i<exp.length();i++)
//         {
//             char c=exp.charAt(i);
//             if(c == ' ')
//                 continue;
              
//             // If the scanned character is an operand (number here),
//             // push it to the stack.
//             if(Character.isDigit(c))
//             stack.push(c - '0');
              
//             //  If the scanned character is an operator, pop two
//             // elements from stack apply the operator
//             else
//             {
//                 int val1 = stack.pop();
//                 int val2 = stack.pop();
                  
//                 switch(c)
//                 {
//                     case '+':
//                     stack.push(val2+val1);
//                     break;
                      
//                     case '-':
//                     stack.push(val2- val1);
//                     break;
                      
//                     case '/':
//                     stack.push(val2/val1);
//                     break;
                      
//                     case '*':
//                     stack.push(val2*val1);
//                     break;
//               }
//             }
//         }
//         return stack.pop();    
//     }
      
//     // Driver program to test above functions
//     public static void main(String[] args) 
//     {

//         String exp1 = "2 3 5 6 + * -";
//         System.out.println(evaluatePostfix(exp1));
        
//         String exp2 = "8 2 7 3 6 1 * - - - +";
//         System.out.println(evaluatePostfix(exp2));
        
//         String exp3 = "7 4 9 8 3 2 2 + + + * * -";
//         System.out.println(evaluatePostfix(exp3));
        
//         String exp4 = "100 200 + 2 / 5 * 7 +";
//         System.out.println(evaluatePostfix(exp4));
        
//         String exp5 = "8 2 7 3 6 1 * - - - +";
//         System.out.println(evaluatePostfix(exp2));
    
//         String exp6 = "7 4 9 8 3 2 2 + + + * * -";
//         System.out.println(evaluatePostfix(exp3));
//     }
// }



import java.util.Stack;

class Mod2OSgraph{
    // Method to evaluate value of a postfix expression
    static int evaluatePostfix(String exp){
        //create a stack
        Stack<Integer> stack = new Stack<>();
        // Scan all characters one by one
        for(int i = 0; i < exp.length(); i++){
            char c = exp.charAt(i);
            if(c == ' ')
                continue;
            // If the scanned character is an operand
            // (number here),extract the number
            // Push it to the stack.

            else if(Character.isDigit(c)){
                int n = 0;
                //extract the characters and store it in num
                while(Character.isDigit(c)){
                    n = n*10 + (int)(c-'0');
                    i++;
                    c = exp.charAt(i);
                }
                i--;
                //push the number in stack
                stack.push(n);
            }
        // If the scanned character is an operator, pop two
        // elements from stack apply the operator
        else{
            int val1 = stack.pop();
            int val2 = stack.pop();
            switch(c){
                case '+':
                    stack.push(val2+ val1);
                    break;
                case '-':
                    stack.push(val2- val1);
                    break;
                case '/':
                    stack.push(val2/ val1);
                    break;
                case '*':
                    stack.push(val2* val1);
                    break;
            
            }
            
        }
            
    }
            
    return stack.pop();

}

    // Driver program to test above functions
    public static void main(String[] args){
            String exp1 = "2 3 5 6 + * -";
            System.out.println(evaluatePostfix(exp1));
            
            String exp2 = "8 2 7 3 6 1 * - - - +";
            System.out.println(evaluatePostfix(exp2));
            
            String exp3 = "7 4 9 8 3 2 2 + + + * * -";
            System.out.println(evaluatePostfix(exp3));
    
            String exp4 = "100 200 + 2 / 5 * 7 +";
            System.out.println(evaluatePostfix(exp4));
            
            String exp5 = "8 2 7 3 6 1 * - - - +";
            System.out.println(evaluatePostfix(exp5));
            
            String exp6 = "7 4 9 8 3 2 2 + + + * * -";
            System.out.println(evaluatePostfix(exp6));
    
    }
}


















