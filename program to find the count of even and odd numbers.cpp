// importing the libraries
#include <bits/stdc++.h>
using namespace std;
// declaring the local variables
int n,j=0; 
int b[2];
int countOdd = 0;
int countEven = 0;
// declaring the function with 3 parameters 
// as mentioned
int* countEvenOdd(int n, int countEven, int countOdd) {
    int a[n]={0};
    // iterating and checking the numbers
    // are even or odd
    for(int i=0;i<n;i++){
        cin>>a[j];
        if(a[j]%2==0) countEven++;
        else countOdd++;
    }
    // assining the count of even and odd counts
    b[0] = countEven;
    b[1] = countOdd;
    // returing the result
    return b;
}
// main function
int main(){   
    // getting the size of the array
    cin>>n;
    // function calling 
    int *result = countEvenOdd(n,countEven,countOdd);
    // displaying the result
    cout<<"You entered "<<result[0]<<" even numbers(s) and "<<result[1]<<" odd number(s)..";
}

