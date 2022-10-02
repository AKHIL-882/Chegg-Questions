/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int myfunction1(){
    return 1;
}
int myfunction2(){
    return 2;
}
int myfunction3(){
    return 3;
}

int main()
{
    int x = myfunction1();
    int y = myfunction2();
    int z = myfunction3();
    printf("%d,%d,%d",x,y,z);
    printf("\n");
    
    double dx = (double)x;
    double dy = (double)y;
    double dz = (double)z;
    printf("%f,%f,%f",dx,dy,dz);
    printf("\n");
    
    unsigned ux = x;
    unsigned uy = y;
    printf("%f",dx+dy);
    printf("\n");
    printf("%f",(double)(y+x));
    printf("\n");
    printf("%d",dx + dy == (double)(y+x));

}

