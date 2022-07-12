/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
int f0(int *a, int b){
    *a = b+52;
    a = &b;
    printf("%d %d\n",*a,b);
    return(102);
}

int f1(int *a,int b){
    a=&b;
    *a=b+52;
    printf("%d %d\n",*a,b);
    return(102);
}

int main()
{
    int b,c,*d,*e;
    d= &b;
    e = &b;
    b = 104;
    *d = 15;
    c = 134;
    f1(e,*e);
    printf("\n ==> result 1: %d %d %d %d \n",b,c,*d,*e);
    for(int x=0;x<4;x++){
        printf("%d %d\n",x,*d);
        d[0] = x+17;
        printf("%d %d\n",x,*d);
    }
    printf("\n ==> result 2: %d %d %d %d \n",b,c,*d,*e);
    *d = -10;
    f0(e,b);
    printf("\n ==> result 3: %d %d %d %d \n",b,c,*d,*e);
    d = &c;
    e = &b;
    printf("\n ==> result 4: %d %d %d %d \n",b,c,*d,*e);
    c = f0(e,b);
    printf("\n ==> result 5: %d %d %d %d \n",b,c,*d,*e);
    return 0;
    
    
}

