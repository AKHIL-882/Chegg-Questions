// importing the libraries
#include<iostream>
#include<string>
#include<algorithm>
#include<bits/stdc++.h>
#include<iostream>  
using namespace std;  
// main method
int main(){
    // declaring the variables
    std::string strValue ;
    // getting the string from user
    getline(cin, strValue);
    // declaring the constants for replacement
    const char replacewith = 'e';
    const char replace  = 'x';
    // Replace all occurrences of character 'e' with 'x'
    std::replace(strValue.begin(),
                 strValue.end(),
                 replacewith,
                 replace);
    // displaying the result
    std::cout<< strValue << std::endl;
}
