// importing the libraries
import java.util.*;
// declaring the main class
public class Main {
    // initializing the main code.
	public static void main(String[] args){
	    int size;
	    // scanner class
	    Scanner sc = new Scanner(System.in);
	    System.out.print("Enter the size of the array: ");
	    // getting the size of the array
	    size = sc.nextInt();
	    // initializeing the array
	    int[] initializedArray = new int[size];
	    System.out.println("Enter the values into arry ");
	    // getting the array values
	    for(int i=0; i < size; i++) {
          // read input
          initializedArray[i] = sc.nextInt();
	    }
		int minValue = initializedArray[0];
		// iterating and finding the Smallest value
		for (int i = 0; i < initializedArray.length; i++) {
			if (initializedArray[i] < minValue)
				minValue = initializedArray[i];
		}
		// displaying the result
		System.out.println("Smallest element present in given array: "+ minValue);
	}
}
