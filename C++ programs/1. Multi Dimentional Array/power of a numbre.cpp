// importing the libraries
#include <iostream>
using namespace std;
// main function
int main(){
    // declaring the variables
    int base, expo, i, result = 1;
    cout << "Please enter number:";
    cin >> base;
    cout << "Please enter number:";
    cin >> expo;
    // calculating base^exponent by repetitively multiplying base
    for(i = 0; i < expo; i++){
        result = result * base;
    }
    // displaying the result
    cout << "Result of " <<base << " raised to the power of " << expo << ": " << result;
    return 0;
}