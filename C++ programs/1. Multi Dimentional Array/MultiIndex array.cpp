// importing the libraries
#include <iostream>
using namespace std;
// function to multiply with index
void multiIndexValue(int arr[]){
    cout<<"Index-multipled array value: ";
    // displaying the result
    for(int i=0; i < 10; i++){
        cout<<arr[i] <<" ";
    }
}
int main(){
    // declearing a array of size 10
    int arr[10];
    // getting input in array from user
    for(int i=0; i < 10; i++){
        cout<<"Please enter value #" << i+1 <<": ";
        cin>>arr[i];
    }
    // ptinting original array
    cout<<"Original Array value: ";
    for(int i=0; i < 10; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    
    // array to store Index-multipled
    int resutArrayValue[10];
    for(int i=0; i < 10; i++){
        resutArrayValue[i]= arr[i] * i;
    }
    
    // function calling
    multiIndexValue(resutArrayValue);
    return 0;
}