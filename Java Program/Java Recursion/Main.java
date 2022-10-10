/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
import java.util.*;
public class Main{
    // main method
	public static void main(String[] args) {
	    // scanner class
	    Scanner sc = new Scanner(System.in);
	   // String userName = sc.nextLine();
	    // display name statically
		System.out.println("Rose Smith");
		System.out.println("Enter the grade: ");
		// getting grade from user
		int grade = sc.nextInt();
		// conditions checking
		if(grade<60 && grade>=40){
		    if(grade<45){
		        System.out.println("fail");
		    }
		    System.out.println("failing");
		}else if (grade>=60 && grade<70) {
		     System.out.println("D+");
		}else if (grade>=70 && grade<80) {
		     System.out.println("B");
		}else if (grade>=80 && grade<90) {
		     System.out.println("B+");
		}else if (grade>=90 && grade<100) {
		    if(grade>95){
		        System.out.println("excellent");
		    }
		     System.out.println("A+");
		}else{
		    System.out.println("Invalid mark!");
		}
		
	}
}
