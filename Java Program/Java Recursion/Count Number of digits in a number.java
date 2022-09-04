// importing the libraries
import java.util.*;
import java.io.*;
// main class
class Main{
    // declaring the main method
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		// getting input from user
		int n = sc.nextInt();
		if(n>=0 && n<=999999){
		    int count=0;
    		// interating over the digits
    		while (n != 0) {
    			n = n / 10;
    			count+=1;
    		}
    		// displaying the result
    		System.out.println(count);
		}else{
		    System.out.println("Out of range");
		}
	}
}

