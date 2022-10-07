// importing the libraries
#include <iostream>
#include  <bits/stdc++.h>
#include <string>
using namespace std;
#define MAX_NAME_LEN 100
// function to count the character
int count(string s, char c){
    int res = 0;
    // iterating over the string
    for (int i=0;i<s.length();i++)
        if (s[i] == c)
            res++;
    // returing the result
    return res;
}
// main function
int main(){
    // declaring the array
    char str[MAX_NAME_LEN],c;
    // getting the character from user
    cin >> c;
    // getting the string from usre
    cin.getline(str, MAX_NAME_LEN);
    // condition checking and displaying the result
    if(count(str, c) == 1){
        cout << count(str, c) << " " << c << endl;
    }else{
        cout << count(str, c) << " " << c <<"\'s" << endl;
    } 
    return 0;
}