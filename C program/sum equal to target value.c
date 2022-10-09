/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
// importing the libraries
#include <stdio.h>
// global variables
int nums[100],numsSize,i,j,target;
// function declaration
int *twoSum(int * nums, int numsSize, int target){
    // iterating over the array
    for(i=0;i<numsSize;i++){
        for(j=i+1;j<numsSize;j++){
            // checking the sum equal to target or not
            if(nums[i] + nums[j] == target ){
                // dispalying the result
                printf("[%d,%d]",i,j);
            }
        }
    }
    
}
// main method
int main(){
    // getting the array size from user
    printf("Enter the size of array: ");
    scanf("%d",&numsSize);
    // getting the element from user
    for(i=0;i<numsSize;i++){
        printf("Enter the element: ");
        scanf("%d",&nums[i]);
    }
    // getting the target value from user
    printf("Enter the target value: ");
    scanf("%d",&target);
    // function calling
    twoSum(nums,numsSize,target);
    
}
