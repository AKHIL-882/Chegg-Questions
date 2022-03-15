import java.util.*;
public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();

        // true if number is less than 0
        if (number < 0 || number == 0)
            System.out.println("\nNumber is either zero or negative");

        // true if number is greater than 0
        else if( number >=1){
            System.out.println("Number is " + number);
            // finding factors
            for (int i = 1; i <= number; ++i) {
              if (number % i == 0) {
                System.out.print(i + ",");
              }
            }
            System.out.println("\n");
            for(int i = 1; i <= 10; i++) {
			// Display multiples
			System.out.print(number * i+ ",");
		    }
        }
    }
}