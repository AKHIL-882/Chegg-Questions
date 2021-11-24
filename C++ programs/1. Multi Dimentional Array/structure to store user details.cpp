
// importing the libraries
#include<iostream>
using namespace std;
// creating a structure with 4 data members
struct userDetails{
        char name[60];
        char lastname[20];
        int age;
        double weight;
};
// initializing the main function
int main(){
        // referrence the variable
        userDetails m;
        // getting the data from user
        cout<<"Enter Name:";
        cin>>m.name;
        cout<<"Enter lastname: ";
        cin>>m.lastname;
        cout<<"Enter age: ";
        cin>>m.age;
        while(m.age<0){
                cout<<"Invalid value\n";
                cout<<"Enter age: ";
                cin>>m.age;       
        }
        cout<<"Enter weight: ";
        cin>>m.weight;
        while(m.weight<0){
                cout<<"Invalid value\n";
                cout<<"Enter weight: ";
                cin>>m.weight;       
        }
        // displaying the result
        cout<<"name: "<<m.name<<endl;
        cout<<"lastname: "<<m.lastname<<endl;
        cout<<"age: "<<m.age<<endl;
        cout<<"weight: "<<m.weight<<endl;
        
        
}