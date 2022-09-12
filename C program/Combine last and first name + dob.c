// importing the libraries
#include <stdio.h>
#include<string.h>
// main method
int main()
{
    // declaring the variables
    char firstname[50], lastname[50],res[100];
    int bir_year,i;
    // getting user inputs
    scanf("%s %s %d",firstname,lastname,&bir_year);
    // finding the length of lastname
    int a=strlen(lastname);
    // slicing the string
    for(i=0;i<=a;i++){
        if(i==5)
            break;
        res[i]=lastname[i];
    }
    // conditions for lastname
    if(a<5){
        res[a] = firstname[0];
    }else{
        res[a-1]=firstname[0];
    }
    // getting the last digits of a number
    int d[10],j=0,reverse = 0, remainder;
    while (bir_year != 0) {
        remainder = bir_year % 10;
        d[j] = bir_year%10;
        reverse = reverse * 10 + remainder;
        bir_year /= 10;
        j++;
    }
    // displaying the result
    printf("Your login name: %s%d%d \n", res,d[1],d[0]);
}