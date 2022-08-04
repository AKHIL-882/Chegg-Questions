// importing the libraries
import java.util.*;
// main class
class Main {
    // define the method
    public static String removeNonAlpha(String userString){
        // replacing non-alphabetic charactes with space
        userString = userString.replaceAll(
          "[^a-zA-Z]", "");
        // returing the result
        return userString;
    }
    // main 
    public static void main(String args[]){
        // defining the scanner class
        Scanner sc = new Scanner(System.in);
        // getting the user input
        String userString = sc.nextLine();
        // displaying the result
        System.out.println(removeNonAlpha(userString));
    }
}