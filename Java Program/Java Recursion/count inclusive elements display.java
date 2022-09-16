// importing the libraries
import java.util.*;
// main class
public class Main {
    // static method allMatches
    public static int[] allMatches(int[] values, int size, int a, int b) {
        int count = 0;
        for (int i = 0; i < size; i++) {
            if(values[i] >= a && values[i] <= b){
                count++;
            }
        }
        // arrya 
        int result[] = new int[count];
        count = 0;
        // appending the values
        for (int i = 0; i < size; i++) {
            if(values[i] >= a && values[i] <= b){
                result[count++] = values[i];
            }
        }
        return result;
    }
    
    // main function
    public static void main(String[] args) {
        // array
        //int[] a = {11, 3, 9, 4, 2, 5, 4, 7, 6, 0};
        int n;
        Scanner sc=new Scanner(System.in);  
        System.out.print("Enter the size of array: ");  
        n=sc.nextInt();  
        // creates an array in the memory of length 10  
        int[] a = new int[n];  
        System.out.println("Enter the elements of the array: ");  
        for(int i=0; i<n; i++){  
            //reading array elements from the user   
            a[i]=sc.nextInt();  
        }  
        System.out.print("Enter the size : ");  
        int s = sc.nextInt(); 
        System.out.print("Enter the value 1: ");  
        int n1 = n=sc.nextInt(); 
        System.out.print("Enter the value 2: ");  
        int n2 = n=sc.nextInt(); 

        // function calling
        int[] returnedArray = allMatches(a, s, n1, n2);
        
        // displaying the result
        for (int i = 0; i < returnedArray.length; i++)
            System.out.print(returnedArray[i]+" ");
    }
}

