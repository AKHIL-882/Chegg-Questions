// importing the libraries
import java.util.*;
import java.lang.*;
// defining the main class  
public class Main{
    // function to find the first digit
    public static int firstDigit(int n){
        // looping the getting the first digit
        while (n >= 10) 
            n /= 10;
        // returing the first digit
        return n;
    }
    // defining the main method
    public static void main(String argc[]){
        int n;
        Scanner sc = new Scanner(System.in);
        // getting input from user
        System.out.print("Enter the number: ");
        n = sc.nextInt();
        // function calling and displaying the result
        System.out.println("The first digit is: "+ firstDigit(n));
    }
}
  