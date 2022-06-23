/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
// declaring the main class
public class Main{
    // declaring the printEvenNumbers method
    public static void printEvenNumbers(int[] array){
        System.out.printf("Even Numbers in the array: ");
        // iterating and finding the even numebrs
        for(int i=0;i<array.length;i++){
            
            if(array[i]%2==0)
                // displaying the result
                System.out.print(array[i] + " ");
        }
    }
    // declaring the main method
	public static void main(String[] args) {
	    // initializing the array
	    int[] array = {7,4,3,2,6,9};
	    // calling the function
	    printEvenNumbers(array);
	}
}
