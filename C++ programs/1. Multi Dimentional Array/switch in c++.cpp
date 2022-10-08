/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************00**********************************************/\
// importing the libraries
#include <iostream>
using namespace std;
// main method
int main(){
    // local variable
    int numberOfBelts;
    cout<< "[Martial Arts Belt] \nWhat belt grade are you? " ;
    // getting input from user
    cin >> numberOfBelts;
    // switch case
    switch (numberOfBelts) {
      case 10:
        cout << "You have a white belt,\nwith 0 stripe!";
        break;
      case 9:
        cout << "You have a white belt,\nwith 1 stripe!";
        break;
      case 8:
        cout << "You have a yellow belt,\nwith 1 stripe!";
        break;
      case 7:
        cout << "You have a yellow belt,\nwith 2 stripe!";
        break;
      case 6:
        cout << "You have a blue belt,\nwith 1 stripe!";
        break;
      case 5:
        cout << "You have a blue belt,\nwith 2 stripe!";
        break;
      case 4:
        cout << "You have a green belt,\nwith 1 stripe!";
        break;
      case 3:
        cout << "You have a green belt,\nwith 2 stripe!";
        break;
      case 2:
        cout << "You have a brown belt,\nwith 1 stripe!";
        break;
      case 1:
        cout << "You have a brown belt,\nwith 2 stripe!";
        break;
      case 0:
        cout << "You have a black belt,\nwith 0 stripe!";
        break;
      default:
        cout << "You have no belt...";
    }
}

