// importing the libraries
#include <iostream>
#include <ctype.h>
using namespace std;
// method to return edited copy of string
string stringEdit(string str) {
    // local variable
    string newString = "";
    // iterating through string
    for (int i = 0; i < str.length(); i++) {
        // if char is a letter, convert it to uppercase and add to new copy
        if (isalpha(str[i])) {
            newString += toupper(str[i]);
        }
    }
    // return edited copy of string
    return newString;
}
int main() {
    // test 1
    // if you need to get the string from user
    string str1;
    cout<<"Enter the string: ";
    getline(cin, str1);
    cout << "String 1: " << str1 << endl;
    cout << "Edited copy of string 1: " << stringEdit(str1) << endl;
    cout << endl;
    // if the string is predefined
    string str2 = "@kingu!@##!Queenji145";
    cout << "String 2: " << str2 << endl;
    cout << "Edited copy of string 2: " << stringEdit(str2) << endl;

}