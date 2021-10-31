// importing the libaries
#include <iostream>
using namespace std;
// defining the structure
struct Numbers {
    int num1;
    int num2;
    int num3;
    
};
// Function declaration
int MIN(Numbers);
// initializing the main function
int main() {
    Numbers p1;
    // getting values from user
    cin>>p1.num1;
	cin>>p1.num2;
	cin>>p1.num3;
    // Function call with structure variable as an argument
    MIN(p1);
    return 0;
}

int MIN(Numbers p1) {
    // conditions for finding the smallest value
    if (p1.num1 <= p1.num2 && p1.num1 <= p1.num3)
      cout << p1.num1 << " is smallest" << endl;
    else if (p1.num2 <= p1.num1 && p1.num2 <= p1.num3)
      cout << p1.num2 << " is smallest" << endl;
    else
      cout << p1.num3 << " is smallest" << endl;
    return 0;
}