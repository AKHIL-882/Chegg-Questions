
// importing the libraries
import java.util.*;
// declaring the main class
public class Main{   
    // declaring the function to convert digit to hexadecimal
    public static char hexadecimalConvertor(int digit){
        char ch = (char)(digit+'0');
        // we know in hexadecimal the values of
        // A,B,C,D,E,F are 10,11,12,13,14,15 respectively
        if(digit == 10)
            ch = 'A';
        else if(digit == 11)
            ch = 'B'; 
        else if(digit == 12)
            ch = 'C'; 
        else if(digit == 13)
            ch = 'D'; 
        else if(digit == 14)
            ch = 'E'; 
        else if(digit == 15)
            ch = 'F'; 
        return ch;
    }
    // converting the number into human readable
    public static String toRleString(byte[] rleData){
    // local variable
    String result = "";
    for(int i=0;i<rleData.length;i+=2){
        if(i!=0)
            result = result + ":";
        result = result + rleData[i] + hexadecimalConvertor(rleData[i+1]);
        }
    return result;
    }
    // definiing the main method
    public static void main(String[] args) {
      // displaying the result
       System.out.println("Human Readable string = "+toRleString(new byte[]{15,15,6,4}));
    }
}