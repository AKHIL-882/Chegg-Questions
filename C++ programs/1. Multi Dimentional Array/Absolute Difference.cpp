// importing libraries
#include<bits/stdc++.h>
using namespace std;
// function declaration
void closestNumbers(int arr[], int n){
    if (n <= 1)
    	return;
    // sorting the array
    sort(arr, arr+n);
    
    // absolute difference
    int minDiff = arr[1] - arr[0];
    
    for (int i = 2 ; i < n ; i++)
    	minDiff = min(minDiff, arr[i] - arr[i-1]);
    	
    // traversing the array 
    for (int i = 1; i < n; i++)
    	if ((arr[i] - arr[i-1]) == minDiff)
    		cout << arr[i-1] << " " << arr[i] << "\n";
}

// main method
int main(){
    // array declaration 
	int arr[] = {6,2,4,10};
	// declarating the size
	int n = sizeof(arr) / sizeof(arr[0]);
	// function calling
	closestNumbers(arr, n);
	return 0;
}
