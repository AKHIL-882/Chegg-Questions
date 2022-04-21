// importing the libraries
#include<iostream>
#include<stack>
#include<string>
using namespace std;
// checking the brackets are paired or not
bool bracketspairs(char openBracket,char closeBracket){
	if(openBracket == '(' && closeBracket == ')') return true;
	else if(openBracket == '{' && closeBracket == '}') return true;
	else if(openBracket == '[' && closeBracket == ']') return true;
	return false;
}
// checking the brackets are balanced
bool balancedBrackets(string exp){
    // declaring the stack
	stack<char>  S;
	// looping the string
	for(int i =0;i<exp.length();i++){
		if(exp[i] == '(' || exp[i] == '{' || exp[i] == '[')
		    // pushing the brackets
			S.push(exp[i]);
		else if(exp[i] == ')' || exp[i] == '}' || exp[i] == ']'){
		    // comparing the brackets
			if(S.empty() || !bracketspairs(S.top(),exp[i]))
				return false;
			else
			    // popping the bracket
				S.pop();
		}
	}
	// checking the brackets
	return S.empty() ? true:false;
}
// declaring the main method
int main(){
	string userString;
	cout<<"Enter an userString:  ";
	cin>>userString;
	if(balancedBrackets(userString))
		cout<<"True\n";
	else
		cout<<"False\n";
}