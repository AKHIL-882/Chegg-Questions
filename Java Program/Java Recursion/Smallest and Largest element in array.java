// importing 
import java.util.*;
// main class
class Main{
    // main method
    public static void main(String args[]){
        // declaring the variables
        int large,small;
        int[] a = new int[5];
        int n = a.length;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the elements into array:\n " );
        for(int i=0; i<n; i++){  
            a[i]=sc.nextInt();  
        }  
        // getting the size of the array
        large=small=a[0];
        // iterating over the array
        for(int i=1;i<n;++i){
            // comparing and getting the large values
            if(a[i]>large)
                large=a[i];
            // camparing and getting the smallest value
            if(a[i]<small)
                small=a[i];
        }
        // displaying the smallest and largest element in array
        System.out.print("The smallest element: " + small );
        System.out.print("\nThe largest element:  " + large );
    }
}