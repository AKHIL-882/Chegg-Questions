// importing the libraries
#include <iostream>
#include <string.h>
using namespace std;
// main method
int main(){
    // string array
    char str[100];
    // getting input from user
    cin>>str;
    // displaying the string
    cout<<str<<'\n';
    // displaying the string in reverse order
    // by character by character
    for(int i = (strlen(str) - 1); i >= 0; i--)
        cout <<str[i] << '\n';
    return 0;
}