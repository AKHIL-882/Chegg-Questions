// importing the libraries
#include <iostream>
#include <stack>
#include <iterator>
#include <map>
#include <string>
#include <bits/stdc++.h>
using namespace std;
// fuunction to check the balanced 
// parentheses, brackets, and braces
bool balancedPatenBraketsBraces(string expr){
    // creating a stack
	stack<char> s;
	char x;
	// traversing the Expression
	for (int i = 0; i < expr.length(); i++){
		if (expr[i] == '(' || expr[i] == '[' || expr[i] == '{'){
			// pushing the element in the stack
			s.push(expr[i]);
			continue;
		}
		// checking the stack is empty
		if (s.empty())
			return false;
    
		switch (expr[i]) {
		    case ')':
    			x = s.top();
    			s.pop();
    			if (x == '{' || x == '[')
    				return false;
    			break;

		    case '}':
    			x = s.top();
    			s.pop();
    			if (x == '(' || x == '[')
    				return false;
    			break;

	    	case ']':
    			x = s.top();
    			s.pop();
    			if (x == '(' || x == '{')
    				return false;
    			break;
		}
	}https://www.onlinegdb.com/online_c_compiler#tab-stdin
	return (s.empty());
}

// initialze the main function
int main(){
	string expr;
	// getting user input
	getline(cin, expr);

	// function calling and display result
	if (balancedPatenBraketsBraces(expr))
		cout << "Balanced";
	else
		cout << "Not Balanced";
	return 0;
}
