/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

typedef struct a1{
    int al,be,*ga;
}a1;


typedef struct b1{
    int al,be;
}b1;


void f1(b1 a){
    printf("\n In F1 => %d %d \n ",a.al,a.be);
    a.al = 0;
    a.be = 1;
    printf("\n In F1 => %d %d \n",a.al,a.be);
}

void f2(int a,int b){
    printf("\n In F2 => %d %d \n",a,b);
    a = 0;
    a = 1;
    printf("\n In F2 => %d %d \n",a,b);
}

void f3(b1 a, b1 *b){
    
    printf("\n In F3 => %d %d %d %d \n", a.al,a.be,b->al,b->be);    
    a.be = 4;
    b->al=9;
    printf("\n In F3 => %d %d %d %d \n",a.al,a.be,b->al,b->be);
}



int main()
{
    a1 one;
    b1 six, four;
    one.al = 7; one.be = 11;
    six.al = 101; six.be = 15;
    four.al=4; four.be=15;
    printf("\n In Main => %d %d\n",one.al,one.al);
    printf("\n In Main => %d %d\n",four.al,four.be);
    printf("\n In Main => %d %d\n",six.al,six.be);
    f3(four,&six);
    printf("\n In Main => %d %d\n",one.al,one.al);
    printf("\n In Main => %d %d\n",four.al,four.be);
    printf("\n In Main => %d %d\n",six.al,six.be);
    f2(six.be,four.al);
    printf("\n In Main => %d %d\n",one.al,one.al);
    printf("\n In Main => %d %d\n",four.al,four.be);
    printf("\n In Main => %d %d\n",six.al,six.be);
    f1(six);
    printf("\n In Main => %d %d\n",one.al,one.al);
    printf("\n In Main => %d %d\n",four.al,four.be);
    printf("\n In Main => %d %d\n",six.al,six.be);
    return 0;
}
