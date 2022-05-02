/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
// importing the libraries
#include <stdio.h>
int main(){
    // declaring the variables
    int arr[10],evenCount=0,oddCount=0,i;
    // getting the values from user
    for(i=0;i<10;i++){
        scanf("%d",&arr[i]);
    }
    for(i=0;i<10;i++){
        // finding the even values
        if(arr[i]%2==0){
            evenCount+=1;
        }else{
            // incrementing the odd count
            oddCount+=1;
        }
    }
    // displaying the odd and even counts
    printf("The even count of numbers:%d \n",evenCount);
    printf("The odd count of numbers:%d \n",oddCount);
}
