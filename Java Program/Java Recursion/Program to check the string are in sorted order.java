// importing the libraries
import java.util.*;
import java.io.*;

public class Main {
	// Main method //
	public static void main(String[] args) throws Exception {
		// Creatint a file 
		File file = new File("SortedStrings.txt");
		// checking whether the file is present or not.
		if (!file.exists()) {
			System.out.println(file.getName() + " does not exist");
			System.exit(0);
		}
		System.out.println("File " + file.getName());
		boolean dataSorted = true;
		String string1 = ""; 
		String string2 = "";
		try (
		    // scanner class
			Scanner input = new Scanner(file);
		) {
			// reading the string from file
			if (input.hasNext())
				string1 = input.next();

			while (input.hasNext() && dataSorted) {
				string2 = input.next();
				// display the first two strings which are 
				// out of order
				if (string1.compareTo(string2) > 0) {
					System.out.println(
						"The strings " + string1 + " and " + string2 + " are out of order");
					dataSorted = false;
				}
				string1 = string2;
			}
		}

		// Display whether the strings in the files are stored in increasing order
		if (dataSorted) {
			System.out.println("The strings in the file are stored in increasing order");
		}
	}
}