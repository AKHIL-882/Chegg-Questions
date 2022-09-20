// importing the libraries
import java.util.*;
import java.io.*;
// main class
class Main{
    
    // Function to find nth magic number
    static int functionMagicNumber(int n){
        // local variables
    	int pow = 1, answer = 0;
    	// looping over the number
    	while (n != 0){
        	pow = pow*5;
        	// If last bit of n is set
        	if ((int)(n & 1) == 1)
        		answer += pow;
        	// proceed to next bit
        	// or n = n/2
        	n >>= 1;
    	}
    	// returing the result
    	return answer;
    }

    // main method
    public static void main(String[] args){
        // scanner class
        Scanner sc = new Scanner(System.in);
        // getting input from user
    	int n = sc.nextInt();
    	// function calling and displaying the result
    	System.out.println(functionMagicNumber(n));
    }
}
