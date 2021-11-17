// importing the libraries
import java.util.*;
public class Main {
    // local variables
    static Object lock = new Object();
    static Integer count = 1;
    static String flag;
    public static void main(String[] args) {
      // getting the inputs from user
      Scanner scanner = new Scanner(System.in);
      System.out.print("Enter the Letter1: ");
      char userLetter1 = scanner.next().charAt(0);
      System.out.print("Enter the Letter2: ");
      char userLetter2 = scanner.next().charAt(0);
      System.out.print("Enter the Letter3: ");
      char userLetter3 = scanner.next().charAt(0);
      // converting the character to string
      String userLetter1Str=String.valueOf(userLetter1); 
      String userLetter2Str=String.valueOf(userLetter2); 
      String userLetter3Str=String.valueOf(userLetter3); 
      // creating the threads
      Thread t1 = new Thread(new SimultaneousRun(userLetter1Str));
      Thread t2 = new Thread(new SimultaneousRun(userLetter2Str));
      Thread t3 = new Thread(new SimultaneousRun(userLetter3Str));
      // starting the threads
      t1.start();
      t2.start();
      t3.start();

    }

    // implementing the Runnable
    static class SimultaneousRun implements Runnable {
      String threadLetter;
      static List<String> letters = new ArrayList();

      SimultaneousRun(String letter){
        this.threadLetter = letter;
        letters.add(letter);
        if (flag == null || flag == "")
          flag = letter;
      }

       
      private String getNextFlag(String flag){
        int index = letters.indexOf(flag);
        if (index == letters.size() - 1)
          return letters.get(0);
        else
          return letters.get(index + 1);
      }

      public void run(){
        try{
          while (true){
            Thread.sleep(500);
            synchronized (lock){
              printPattern();
            }
          }
        }catch(InterruptedException e) {
          e.printStackTrace();
        }

      }
      // method to print pattern
      private void printPattern() throws InterruptedException {
        if (flag != threadLetter) {
            lock.wait();
        }else{
          int startIndex = count;
          for (int i = 0; i < 3; i++) {
            System.out.println(new String(new char[startIndex]).replace("\0", threadLetter));
            startIndex += 1;
          }
         if(letters.get(letters.size() - 1) == threadLetter)
            count += 3;
            flag = getNextFlag(threadLetter);
            lock.notifyAll();
          }
        }
    }
}