import java.util.*;
import java.io.*;
// A BST node
class Node {
	int data;
	Node left, right;
	Node(int x)
	{
		data = x;
		left = right = null;
	}
}
class Main {
	static int count = 0;
	// recursive function to insert an key into BST
	public static Node insert(Node root, int x){
		if (root == null)
			return new Node(x);
		if (x < root.data)
			root.left = insert(root.left, x);
		else if (x > root.data)
			root.right = insert(root.right, x);
		return root;
	}
	// function to find the smallest element
	public static Node getSmallestElement(Node root, int k){
		// base case
		if (root == null)
			return null;
		// search in left subtree
		Node left = getSmallestElement(root.left, k);
		// if smallest is found in left subtree, return it
		if (left != null)
			return left;
		// if current element is k'th smallest, return it
		count++;
		if (count == k)
			return root;
		// else search in right subtree
		return getSmallestElement(root.right, k);
	}
	// Function to find display the smallest element in BST
	public static void printgetSmallestElement(Node root, int k){
		count = 0;
		Node res = getSmallestElement(root, k);
		if (res == null)
			System.out.println("Null");
		else
			System.out.println(res.data);
	}
	public static void main (String[] args) {
		Node root = null;
		// Uncomment the bolow code if you want to take inputs
		// from user
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter the size of the array: :");
		int size = sc.nextInt();
		int[] keys = new int[size];
		System.out.println("Enter the values of the array: :");
		for(int i=0; i < size; i++) {
          keys[i] = sc.nextInt();
        }

       // use the below code if you want to preintialize
       // the array.
	   // int keys[] = { 20,8,22,4,12,10,14 };
		for (int x : keys)
			root = insert(root, x);
		int k = 1;
		printgetSmallestElement(root, k);
		
	}
}
