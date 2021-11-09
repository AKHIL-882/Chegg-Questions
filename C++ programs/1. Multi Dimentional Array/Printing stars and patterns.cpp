// importing the libraries
#include <iostream>
using namespace std;
// initializing the main method
int main(){
    int arr[5];
    // getting values from user
    for(int i=0;i<5;i++){
        cin>>arr[i]; 
    }
    // iterating over the values
    for(int i=5;i>0;i--){
      // printing the stars
        for(int j=i;j>0;j--){ 
            cout<<"*";
        }
        // printing white spaces
        for(int j=1;j<=5-i;j++) {
            cout<<" ";
        }
        cout<<" "; 
        // printing the hypens
        std::cout<< std::string(arr[5-i],'-');
        cout<<endl;
    }
    return 0;
}