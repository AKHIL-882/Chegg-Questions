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
	    // scanner class
		Scanner sc = new Scanner(System.in);
		System.out.println("This program prints odd and even numbers between LB and UB. ");
		System.out.println("Enter Lower and Upper bound (integers) ");
		// getting input from user
		int lower = sc.nextInt();
		int upper = sc.nextInt();
		System.out.println("Even Numbers:");
		// printing the even values
		for(int i=lower;i<=upper;i++){
		    if(i%2==0){
		        System.out.print(i + ", ");
		    }
		}
		System.out.println("\nOdd Numbers:");
		// printing the odd values
		for(int i=lower;i<=upper;i++){
		    if(i%2!=0){
		        System.out.print(i + ", ");
		    }
		}
		
	}
}
