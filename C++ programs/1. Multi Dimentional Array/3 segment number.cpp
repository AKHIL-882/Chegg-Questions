// importing the libraries
#include <iostream>
using namespace std;
// intialzing the main function
int main() {
    // local variables
    int p = 1000000000, number, d;
    // getting value from the user
    cout << "Please enter an integer number: ";
    cin >> number;
    // checking the conditions
    if (number > 0){
        cout << "3-digit Segment(s):" << endl;
        while (p >= 1) {
            d = number / p;
            if (d > 0) {
                if (d < 10) {
                    cout << "00" << d;
                } else if (d < 100) {
                    cout << "0" << d;
                } else {
                    cout << d;
                }
                d = d % 10;
                cout << " ";
                // displaying the values
                if (d == 0) {
                    cout << "Zero" << endl;
                } else if (d == 1) {
                    cout << "One" << endl;
                } else if (d == 2) {
                    cout << "Two" << endl;
                } else if (d == 3) {
                    cout << "Three" << endl;
                } else if (d == 4) {
                    cout << "Four" << endl;
                } else if (d == 5) {
                    cout << "Five" << endl;
                } else if (d == 6) {
                    cout << "Six" << endl;
                } else if (d == 7) {
                    cout << "Seven" << endl;
                } else if (d == 8) {
                    cout << "Eight" << endl;
                } else if (d == 9) {
                    cout << "Nine" << endl;
                }
            }
            // getting the remainder the number
            number = number % p;
            p /= 1000;
        }
    }
    return 0;
}