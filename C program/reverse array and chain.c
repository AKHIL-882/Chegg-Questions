// importing the libraries
#include <stdio.h>
// initializing the main method
int main(){
    // local variables
    int count = 0;
    int a[100];
    do {
        // getting input from the user
        scanf("%d", &a[count++]);
    } while (getchar() != '\n' && count < 100);
    a[count];
    
    if(a[0]==0)
        printf("no chain");
    else{
        // display the array in reverse order
        for(int i = count-2; i >= 0; i--){
            printf("%d ", a[i]);
        }
    }
    return 0;
}