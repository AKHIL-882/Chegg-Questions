// importing the libraries
using System;
public class Program{
    // main method
	public static void Main(string[] args){
	    // local variables
		int i, sum = 0;
		string val;
        int res;
        // getting the size of array from user
		Console.WriteLine("Enter the size of array: ");
        val = Console.ReadLine();
        res = Convert.ToInt32(val);
        int[] arr = new int[res];
        // getting the array element from user
		Console.Write("Enter numbers into array:\n");
		for (i = 0; i < arr.Length; i++){
			arr[i] = Convert.ToInt32(Console.ReadLine());
		}
		// finding the even value which are at odd locations
		// and calculating the sum
		for (i = 0; i < res; i++){
		    if(i%2!=0){
		        if(arr[i]%2==0){
		            sum = sum + arr[i];
		        }
		    }
		}
		// displaying the result
		Console.WriteLine("The sum of even numbers in odd location is:" + sum);
	}
}