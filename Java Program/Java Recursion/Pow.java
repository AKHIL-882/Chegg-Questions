/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
import java.util.*;
import java.lang.Math;
public class MathFunctions
{
	public static void main(String[] args) {
		Scanner scnr = new Scanner(System.in);
		double x;
		double y;
		double z;
		
		x = scnr.nextDouble();
		y = scnr.nextDouble();
		// CODE FOR THE QIVEN EQUATION
		z = Math.abs(Math.pow(y, 3.0)-x);
		
		System.out.printf("%.1f\n",z);
	}
}
