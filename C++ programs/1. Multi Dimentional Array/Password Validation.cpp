// importing the libraries
#include <iostream>
#include<bits/stdc++.h>
using namespace std;

bool passwordCheck(string userString){
    int i,c=0,s=0,d=0;
    // checking length of the string
    if(!(userString.length()>=8))
        return false;
    // checking uppercase letter is present or not
    for(i=65;i<=90;i++){
        char x = (char)i;
        string str1(1,x);
        if(userString.find(str1)!=std::string::npos)
            c=1;
    }
    if(c==0)
        return false;
    // checking if small letter are present or not
    for(i=90;i<=122;i++){
        char x = (char)i;
        string str1(1,x);
        if(userString.find(str1)!=std::string::npos)
            s=1;
    }
    if(s==0)
        return false;
    // checking for digit
    for(i=0;i<=9;i++){
        string str = to_string(i);
        if(userString.find(str)!=std::string::npos)
            d=1;
    }
    if(d==0)
        return false;
    return true;
}
// initializing the main function
int main(){
    bool flag;
    string password;
    // getting the password from user
    cout<<"Enter a password: ";
    cin>>password;
    flag = passwordCheck(password);
    // displaying the result
    if(flag)
        cout<<"Valid password";
    else
        cout<<"Invalid password";

    return 0;
}