// importing the libraries
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> 
#include <pthread.h>
int global[1];

// function to get the factorial
void *sum_thread(void *arg){
    int j,n,*args_array;
    args_array = arg;
    n=args_array[0];
    long int fac=1;
    for(j=1;j<=n;j++) {
        fac=fac*j;
    }
    printf("\nFactorial of %d is %ld",n,fac);
    return NULL;
}

// function to print message
void *print_thread(){
    printf("\nI am a thread that runs forever\n");
    return NULL;
}

// initializing the main method
int main(){
    // local variabls
    pthread_t tid_fact,tid_print;
    int i;
    for (i = 0; i < 3; i++){
        scanf("%d",&global[0]);
        // calling the threads
        pthread_create(&tid_fact,NULL,sum_thread,global);
        pthread_create(&tid_print,NULL,print_thread,global);
    }
    pthread_exit(NULL);

    return 0;
}