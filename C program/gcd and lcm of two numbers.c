#include<stdio.h>
int main(){
    // local variables
    int num1=46, num2=59, gcd, lcm, remainder, numerator, denominator;
    // checking the conditions for gcd
    if (num1 > num2){
        numerator = num1;
        denominator = num2;
    }
    else{
        numerator = num2;
        denominator = num1;
    }
    remainder = numerator % denominator;
    // finding the lcm
    while (remainder != 0){
        numerator   = denominator;
        denominator = remainder;
        remainder   = numerator % denominator;
    }
    gcd = denominator;
    lcm = num1 * num2 / gcd;
    // displaying the result
    printf("GCD of %d and %d = %d\n", num1, num2, gcd);
    printf("LCM of %d and %d = %d\n", num1, num2, lcm);
}