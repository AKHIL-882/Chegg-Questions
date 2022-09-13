import java.util.*;

// Class definition
public class MovieQuoteInfo{
  //main method definition
  public static void main(String[] args){
      Scanner sc = new Scanner(System.in);
       // Declare and initialize the string variables
       // use the below assingments if you want to assign 
       // statically
       
        // String movieQuote = "Rosebud";
        // String saidBy = "Charles Foster Kane";
        // String movieName = "Citizen Kane";
        // String releasedYear = "1941";
        
        String movieQuote = sc.nextLine();
        String saidBy = sc.nextLine();
        String movieName = sc.nextLine();
        int releasedYear = sc.nextInt();
        
        
        // Displaying the result
        System.out.println("---------------------");
        System.out.println(movieQuote+",");
        System.out.println("said by " +saidBy);
        System.out.println("in the movie " +movieName);
        System.out.println("in " +releasedYear+".");
  }
}