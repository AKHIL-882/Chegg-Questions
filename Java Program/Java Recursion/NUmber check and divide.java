// importing the libraries
import java.util.Scanner;
public class Main{
        // defining the main method
        public static void main(String[] args) {
                Scanner input = new Scanner(System.in);
                // local variables
                int number1 = 0;
                int number2 = 0;
                boolean error = true;
                
                // while loop to get the first number
                while (error) {
                    System.out.print("Enter first number: ");
                    //Checking the input is integer or not
                    if (input.hasNextInt()){
                        //if integer reads to number1 and sets the flag to false
                        number1 = input.nextInt();
                        error = false;
                    }
                    //Else reads as a string not saved 
                    else {
                        input.next();
                    }
                }
                //resetting flag
                error = true;
        
                // while loop to get the second number
                while (error) {
                    System.out.print("Enter second number: ");
                    //Checking the input is integer or not
                    if (input.hasNextInt()){
                        //if integer reads to number2 
                        number2 = input.nextInt();
                        //the flag sets to false only if the input integer is not zero
                        if(number2 != 0){
                            error = false;
                        }
                    }
                    //Else reads as a string not saved 
                    else {
                        input.next();
                    }
                }
            // dividing the numbers and displaying the result
            System.out.println("Solution: "+number1/number2);
            }
}