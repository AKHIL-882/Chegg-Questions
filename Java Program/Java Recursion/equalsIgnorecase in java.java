/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
// importing the libraries
import java.util.*;
// main class
public class Main{
    // main method
	public static void main(String[] args) {
	    // Scanner class
		Scanner sc = new Scanner(System.in);
		// getting user input
		String userInput = sc.nextLine();
		// condition checking and printing the result
		if(userInput.equalsIgnoreCase("AMOS")){
		    System.out.println("It was Amos with the candlestick!");
		}else if(userInput.equalsIgnoreCase("Kevin")){
		    System.out.println("It was Kevin with the revolver!");
		}else if(userInput.equalsIgnoreCase("Juan")){
		    System.out.println("It was Juan with the load pipe!");
		}else{
		   System.out.println("We're not sure who that is. We need to investigate further."); 
		}
		
	}
}
