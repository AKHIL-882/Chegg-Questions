// importing the libraries
#include <iostream>
using namespace std;
// enumeration of educational types
enum Education {Elementary=1, JuniorHigh = 2, SeniorHigh=3, College=4};
// declaring the enumeration
Education Diploma(int userInput){
    // condition for education types
    if (userInput>= 1 && userInput<=5)
        return Elementary;
    else if (userInput>=6 && userInput<=8)
        return JuniorHigh;
    else if (userInput>=9 && userInput<=12)
        return SeniorHigh;
    else if (userInput>=13 && userInput<=16)
        return College;
    else{
        cout<<"Wrong input";
        exit(1);
    }
}
// main method
int main(){
    // local variables
    int userInput, n;
    cout<<"********************* Level Of Diploma ************************"<<endl;
    cout<<"Enter the userInputs of the education: ";
    cin>>userInput;
    cout<<"\nThe level of diploma is: ";
    n = Diploma(userInput);
    switch (n) {
        case 1:
            cout<<"Elementary school Education";
            break;
        case 2:
            cout<<"Junior High School Education";
            break;
        case 3:
            cout<<"High School Education";
            break;
        case 4:
            cout<<"Associate Degree or Bachelor’s Degree";
            break;
        default:
            cout << "Error! The operator is not correct";
            break;
    }
}