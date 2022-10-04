/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
// x = int(input())
// y = int(input())

// if y >= x:
//     for i in range(x, y+1, 5,):
//         print(i, end=' ')
//     print()
// else:
//     print('Second integer can\'t be less than the first.')

// importing the libraries
#include <iostream>
using namespace std;
// main method
int main(){
    // local variables
    int x,y;
    // getting input from user
    cin >> x >> y;
    // checking the result
    if(y>=x){
        // incrementing the value
        for(int i=x;i<=y;i=i+5){
            // displaying the result
            cout<< i << " ";
        }
    }else{
        // displaying the error statement
        cout<< "Second integer can't be less than the first";
    }
}





