// importing the libraries
#include<stdio.h>
// creating structure
struct structureFraction {
    int number;
    int denominator;
}structureFrac;
// function to get the values of neumerator and demoninator
struct structureFraction get_structureFraction() {
    printf("Enter number and denominator: ");
    scanf("%d", &structureFrac.number);
    scanf("%d", &structureFrac.denominator);
    return structureFrac;
}
// displaying the result
void print_structureFraction(struct structureFraction structureFrac) {
    printf("%d/%d", structureFrac.number, structureFrac.denominator);
}
// calculating hte gcd 
int gcd(int a, int b){
    if (b == 0)
        return a;
    return gcd(b, a % b);
}
// calculating the hcf
struct structureFraction reduce_structureFraction() {
    int hcf = gcd(structureFrac.number, structureFrac.denominator);
    structureFrac.number = structureFrac.number/hcf;
    structureFrac.denominator = structureFrac.denominator/hcf;
    return structureFrac;
}
// initializing the main function
int main() {
    // calling the structure
    structureFrac = get_structureFraction();
    print_structureFraction(structureFrac);
    printf(" = ");
    print_structureFraction(reduce_structureFraction());
}
