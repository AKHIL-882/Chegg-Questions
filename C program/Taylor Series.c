// importing the libraries
#include<stdio.h>
#include<math.h>
// initializing the main function
int main(){
    // local variables
    int x,i;
    int fact = 1,n;
    float sum=0;
    // getting the value of x 
    printf("\n\nEnter the value of x in the series :  ");
    scanf("%d",&x);
    // getting the number of terms
    printf("\nEnter the number of terms in the series  :   ");
    scanf("%d",&n);
    printf("1 + ");
    // finding each value of series
    for(i=1;i<n;i++){
        // factorial of the number
        fact = fact*i;
        // sum of values
        sum = sum + (pow(x,i)/fact) ;
        printf("x^%d/%d + ",i,fact);
    }
    sum= sum +1; 
    // displaying the result
    printf("\n\nThe sum of the taylor series is :  %.2f\n\n",sum);
    return 0;
}