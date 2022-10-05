// importing the modules
import java.util.*;
// main class
public class Main {
    // main method
    public static void main (String [] args) {
      // Scanner class
      Scanner scnr = new Scanner(System.in);
      // local variables
      int numRows;
      int numColumns;
      int currentRow;
      int currentColumn;
      char currentColumnLetter;
      // getting input from user
      numRows = scnr.nextInt();
      numColumns = scnr.nextInt();
      // iterating over the rows
      for (int i = 1; i <= numRows; i++) {
         currentColumnLetter = 'A';
         // iterating over the columns
         for (int x = 1; x <= numColumns; x++) {
            // displaying the resul
            System.out.print(i);
            System.out.print(currentColumnLetter + " ");
            currentColumnLetter++;
         }
      }

      System.out.println("");
   }
}