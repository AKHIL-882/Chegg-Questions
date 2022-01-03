import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
public class PasswordChecker {

    private HashTable<Integer, String> table;
        public PasswordChecker() {
            table = new HashTable<>();
            iniHashTable("webster.txt");
        }
    
        private void iniHashTable(String filename) {
            try{
                Scanner in = new Scanner(new File(filename));
                while (in.hasNext()) {
                String value = in.next();
                table.insert(value.hashCode(), value);
                }
            in.close();
            } catch (FileNotFoundException e) {
        e.printStackTrace();
        }
    
    }

    public boolean isGoodPassword(String password) {
        if(password.length() < 8)
            return false;
        String sp[] = password.split("[0-9]+");
        for(String str : sp){
            if(table.contains(str.hashCode()))
            return false;
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println("Please enter a password: ");
        Scanner in = new Scanner(System.in);
        String passWord = in.next();
        in.close();
        PasswordChecker pc = new PasswordChecker();
        if(!pc.isGoodPassword(passWord)) {
            System.out.println("Bad password!");
            System.out.println("Password must be at leasst 8 characters long.");
            System.out.println("Make sure not to use dictionary words.");
        }else{
        System.out.println("Please wait...");
        }
    }
}