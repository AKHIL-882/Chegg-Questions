
#define FUNCTIONS_H
#include <iostream>
#include<set>
using namespace std;
int clusters(const multiset<int> dataArray){
        // checking if multiset is empty
        if(dataArray.size() == 0) 
            return 0;
        set<int> visitedBefore;
        int ans = 0;
        // checking the value is visited or not
        for(const int value : dataArray){
                if(visitedBefore.find(value) != visitedBefore.end())continue;
                else{
                        visitedBefore.insert(value);
                        if(dataArray.count(value) > 1) ans++;
                }
        }
        return ans;
}
// initiaizing the main function
int main(){
    // predefining hte dataArray
    multiset<int> dataArray = {1,2,2,3,4,4};
    cout<<clusters(dataArray);
    multiset<int> anotherdataArray = {2,2,4,6,6,6,6,7,8,9,9,9};
    // displaying the dataArray
    cout<<"\n"<<clusters(anotherdataArray);
    return 0;

}