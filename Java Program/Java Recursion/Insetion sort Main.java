// importing the libraries
import java.util.*;
// declaring the main class
class Main {
    // function to sort the elements
	void sort(int arr[]){
	    // assiging the size of the array
		int n = arr.length;
		for (int i = 1; i < n; ++i){
			int key = arr[i];
			int j = i - 1;
			// sorting the elements
			while (j >= 0 && arr[j] > key){
				arr[j + 1] = arr[j];
				j = j - 1;
			}
			arr[j + 1] = key;
		}
	}
	// function to print the elements
	static void printArray(int arr[]){
		int n = arr.length;
		for (int i = 0; i < n; ++i)
		    // printing the elements
			System.out.print(arr[i] + " ");
		System.out.println();
	}
	// declaring the main function
	public static void main(String args[]){
	    // initializing the scanner
	    Scanner sc = new Scanner(System.in);
	    System.out.println("Enter the size of array: ");
	    // getting the size of the array
	    int arraySize = sc.nextInt();
	    int arr[] = new int[arraySize];
	    // getting value from the user
        System.out.println("Enter the elements: ");
        for(int i = 0; i < arraySize; i++){
            arr[i] = sc.nextInt();
        }
        // calling the main function
		Main ob = new Main();
		// sorting the array
		ob.sort(arr);
		// displaying the array
		System.out.println("The sorted array is: ");
		printArray(arr);
	}
}
