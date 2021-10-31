// importing the libaries
import java.util.Arrays;
// initializing the main class
public class Main {
        // initializing the main method
        public static void main(String[] args) {
                // declaring the methods
                int[] A = {1,2,3,6,5,4};
                int[] B = {1,2,3,6,5,4};
                // displaying the result
                System.out.println("The A array is: " + Arrays.toString(A));
                System.out.println("The A array is: " + Arrays.toString(B));
                System.out.println("The A array passing score is: " + passingScore(A, 70));
                System.out.println("The B array passing score is: " + passingScore(B, 70));
                System.out.println("The A array forward and backward: " + backFoward(A));
                System.out.println("The A array forward and backward: " + backFoward(B));
                System.out.println("The Array A and B are same ? " + sameArray(A, B));
                System.out.println("Copy of array is done? " + sameArray(A, copyArray(A)));
                
        }
        // method for passout score
        public static int passingScore(int A[], int passingScore) {
                int count = 0;
                for(int num : A) count = num >= passingScore ? count + 1 : count;
                return count;
        }
        // method for checking backward and forward
        public static boolean backFoward(int A[]) {
                for(int i=0 ; i<A.length ; i++)
                        if(A[i] != A[A.length-i-1]) return false;
                return true;
        }
        // checking array A and B are of same length
        public static boolean sameArray(int A[], int B[]) {
                if(A.length != B.length) return false;
                for(int i=0 ; i<A.length ; i++)
                        if(A[i] != B[i]) return false;
                return true;
        }
        // method for copy of content from A
        public static int[] copyArray(int A[]) {
                int B[] = new int[A.length];
                for(int i=0 ; i<A.length ; i++)
                        B[i] = A[i];
                return B;
        }
}