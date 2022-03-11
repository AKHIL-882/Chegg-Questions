// importing the libary
import java.util.*;
// declaring the main class
class Result {
	public static String compressWord(String s,int k){
		// Base Case
		if (k == 1){
			String ans = "";
			return ans;
		}

		Stack<findConsecutive> st = new Stack<findConsecutive>();
		int l = s.length();
		int currentChar = 0;
		for (int i = 0; i < l; i++) {
			if (st.size() == 0) {
				st.push(new findConsecutive(s.charAt(i), 1));
				continue;
			}
			if (st.peek().c == s.charAt(i)) {
				findConsecutive p = st.peek();
				st.pop();
				p.currentChar += 1;
				if (p.currentChar == k) {
					continue;
				}
				else {
					st.push(p);
				}
			}
			else {
				st.push(new findConsecutive(s.charAt(i), 1));
			}
		}
		String ans = "";
		while (st.size() > 0) {
			char c = st.peek().c;
			int count = st.peek().currentChar;
			while (count-- > 0)
				ans = c + ans;
			st.pop();
		}
		return ans;
	}

	public static void main(String[] args)
	{
	    Scanner sc = new Scanner(System.in);
		
		String st = sc.nextLine();
		int k = sc.nextInt();
		String ans = compressWord(st,k);
		System.out.println(ans);
	}

	static class findConsecutive {
		char c;
		int currentChar;
		findConsecutive(char c, int currentChar)
		{
			this.c = c;
			this.currentChar = currentChar;
		}
	}
}
