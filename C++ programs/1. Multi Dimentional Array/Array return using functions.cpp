// /******************************************************************************

// Welcome to GDB Online.
// GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
// C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
// Code, Compile, Run and Debug online from anywhere in world.

// *******************************************************************************/
#include <iostream>
using namespace std;
// function prototype
void call(int arr[], int SIZE);
int main()
{
    const int SIZE = 10;
    int myArray[SIZE] = {5,10,15,20,25,30,35,40,45,50};
    int multiplyMe = 5;
    // function call
    call(myArray, SIZE);
     
    for(int i=0;i<SIZE;i++){
        cout << myArray[i] << " ";
    }
    cout << endl;
    return 0;
}
// function definition
void call(int myArray[], int size){
    for(int i=0;i<size;i++){
        myArray[i]=myArray[i]*5;
    }
}





