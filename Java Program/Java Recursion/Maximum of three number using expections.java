
// importing the libraries
import java.util.Scanner;
// definig the main calss
    public class Main {
        static int max(int n,int ArrayMax[]){
            try{
            //Throwing an exception if an array is empty
            if(n==0){
                throw new IllegalArgumentException("Array is Empty! ");
            }
            // if the array contains single elemet
            if(n==1){
                assert n==1:"Single Element Array";
                System.out.println("Maximum element is :"+ArrayMax[0]);
            }
            // if the array contains more than one element
            if(n>=2){
                int maximumElement=ArrayMax[0];
                for (int i = 0; i < ArrayMax.length; i++){
                // check for maximum value
                if(ArrayMax[i] > maximumElement)
                    maximumElement = ArrayMax[i];
            }
            return maximumElement;
      
        }
    }
    // expection handling
    catch(IllegalArgumentException e){
        System.out.println("IllegalArgumentException: Array is Empty");
    }
    
    return 0;
    }

    public static void main(String[] args) {
        int [] ArrayMax = new int [10];
        int maximumElement;
        // getting the size of array
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the size of array: ");
        int n=scan.nextInt();
        if(n==0)
            max(n,ArrayMax); 
        else{
            System.out.println("Enter "+n+" Integers");
        for(int i=0;i<n;i++){
            ArrayMax[i]=scan.nextInt();
        }
        // function calling
        maximumElement=max(n,ArrayMax);
        if (n>=2)
        System.out.println("Maximum value of the given array:" + maximumElement);
        }
    }    
}