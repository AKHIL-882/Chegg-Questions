#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;
int main() {
    // Initialize random number generator.
    srand(time(0));  
   // generating the random numbers
   int randNum1 = rand() % 109 + 431;
   int randNum2 = rand() % 109 + 431;
   int randNum3 = rand() % 109 + 431;
   // displaying the numbers generated
   cout<< "The Random Numbers generated are : " << randNum2 << " "  << randNum2 << " " << randNum3;
   // finding the average of three numbers
   int avgRandNumbers = (randNum1 + randNum2 +  randNum3)/3;
   // displaying the averages
   cout<<"\nThe average of the three numbers are :" << avgRandNumbers;
}
