// importing libraries
import java.util.*;
import java.text.DecimalFormat;
// declaring class
public class Main {
    // method to calculate area of circle
    public static double getArea(double radius) {
        return Math.PI * radius * radius;
    }
    // method to calculate area of rectangle
    public static double getArea(int length, int width) {
        return length * width;
    }
    // method to calculate area of cylinder
    public static double getArea(double radius, double height) {
        return Math.PI * radius * radius * height;
    }

    // main signature
    public static void main(String[] args) {
        // decimal formatter
        DecimalFormat f = new DecimalFormat("##.00");
        
        Scanner sc = new Scanner(System.in);
        // getting parameters from user
        System.out.print("Enter radius to calculate circle area: ");
        double cirRad = sc.nextDouble();
        System.out.print("Enter width to calculate rectangle area: ");
        double recWid = sc.nextDouble();
        System.out.print("Enter width to calculate rectangle area: ");
        double recLen = sc.nextDouble();
        System.out.print("Enter base radius to calculate cylinder area: ");
        double cycBas = sc.nextDouble();
        System.out.print("Enter height to calculate cylinder area: ");
        double cycHei = sc.nextDouble();
        
        
        // Area of a circle
        System.out.print("The area of the circle is: ");
        System.out.println(f.format(Main.getArea(cirRad)));
    
        // Area of a rectangle
        System.out.print("The area of the rectangle is: ");
        System.out.println(f.format(Main.getArea(recLen,recWid)));
    
        // Area of cylinder
        System.out.print("The area of the cylinder is: ");
        System.out.println(f.format(Main.getArea(cycBas,cycHei)));
    }

}
