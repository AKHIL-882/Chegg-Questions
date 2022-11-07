/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
using namespace std;
int main()
{
    double myList[6];
    myList[0]= 2.5;
    for(int i=1;i<6;i++){
        myList[i]=i*myList[i-1];
        if(i>3)
            myList[i]=myList[i]/2;
    }
    cout << myList[3] << endl;
    cout << myList[4] << endl;
    
    int alpha[6] = {5};
    for(int i=1;i<6;i++){
        alpha[i] = i*alpha[i-1];
        alpha[i-1] = alpha[i] - 2 * alpha[i-1];
    }
    for(int i=0;i<2;i++)
    cout << alpha[i] << " ";
    cout << endl;
    
    int a[5] = {5};
    for(int i=0;i<5;i++)
    cout << a[i] << " ";
    cout << endl;
    
    
    double s[3] = {5700,6800,5000};
    double r = 0.01;
    
    for(int i=0;i<2;i++)
    cout << (i+1) << " " << s[i]*r << endl;
    
    
    int j,k;
    int b[3][3] = {7,8,9,4,1,2,3,5,6};
    cout << "\n";
    for(k=4;k<7;k++)
    cout<<b[k%2][k%3] << " ";
    
    int num, sqnum;
    int *np=&num;
    num=2;
    *np=5;
    sqnum=*np*num;
    cout<<num<<" "<<*np<<" "<<sqnum;
    
    
    int n,i(1);
    int *np, *ip;
    np=&n;
    ip=&n;
    *np=5;
    *ip=10;
    cout<<n<<" "<<i;
    
    
    int myint1 = 3, myint2 = 3;
    int *pnt1 = &myint1;
    int *pnt2 = &myint2;
    myint1 = ++(*pnt1) + (*pnt1);
    myint2++;
    myint2 = (*pnt2)*(*pnt2);
    cout<<myint1<<myint2<<endl;
    
    int x=10,count=0;
    while(x!=0){
        x--;
        if(x==4)
        continue;
        count++;
    }
    cout << count;
    
    
    
    
    
    
    
    
    
    
    
    
    
    
} 
