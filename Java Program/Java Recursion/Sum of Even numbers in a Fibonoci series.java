// import the libraries
import java.util.*;
// defining the calss
class Main{
    // defining the function to get the sum 
    // for all even number in the series
    public static Integer evenFibonocciSum(int n){
        int sum=0;
        int a = 0, b = 1, c;
        if (n == 0)
            return a;
        for (int i = 2; i <= n; i++){
            c = a + b;
            a = b;
            b = c;
            if(c%2==0){
                sum = sum+c;
            }
        }
        return sum;
    }
    // defining the main method
    public static void main (String args[]){
        int n;
        // declaring the scanner class
        Scanner sc = new Scanner(System.in);
        // getting the input from the user
        n = sc.nextInt();
        // calling and displaying the result.
        System.out.println(evenFibonocciSum(n));
    }
}
 