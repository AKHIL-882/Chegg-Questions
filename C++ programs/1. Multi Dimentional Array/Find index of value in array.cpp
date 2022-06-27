// importring the libraries
#include <iostream>
using namespace std;
// main method
int main(){
    // local variables
    int n = 5,i;
    int arr[n];
    // getting values from users
    cout << "Enter the values in sorted array either ascending or descending order:\n";
    for (i = 0; i < n; i++) {
        cout << "arr[" << i << "] = ";
        cin >> arr[i]; 
    }
    
 
    int elem;
    // getting the value to be searched
    cout<<"Define a value to be searched from sorted array: \n";
    cin>>elem;
    // iterating the array and finding the match case
    i=0;
    while (i < n){
        if (arr[i] == elem) {
            break;
        }
        i++;
    }
    // displaying the index value
    if (i < n){
        cout << "Element is found at index " << i+1;
    }
    // displaying the information if no element found
    else {
        cout << "Element is not present in the given array";
    }
 
    return 0;
}
