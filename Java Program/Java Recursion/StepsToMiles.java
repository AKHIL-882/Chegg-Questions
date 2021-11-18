// importing the libraries
import java.util.Scanner;
public class Main {
  // calculating the step to miles
  public static double calculateStepMiles(int n) throws Exception {
    // thorw Exception
    if(n<0){
      throw new Exception("Exception: Negative step count entered.");
    }
    // returning number of miles
    return n/2000.0;
  }
  // main method
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    // getting input from user
    int n = in.nextInt();
    try{
      // function calling
      double miles = calculateStepMiles(n);
      // displaying the result
      System.out.printf("%.2f", miles);
      System.out.println();
    }
    catch (Exception e){
      System.out.println(e.getMessage());
    }
  }
}