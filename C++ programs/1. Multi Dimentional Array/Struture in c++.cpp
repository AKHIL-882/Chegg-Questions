// importing the libraries
#include <iostream>
using namespace std;
// creating the structure employee
// you can modify the fields if required
struct employee {
    string ename;
    int age, phn_no;
    int salary;
};
// function to display the result
void display(struct employee emp[], int n){
    cout << "\n";
    cout << "Name\tAge\tPhone Number\tSalary\n";
    // iterating the displaying the result
    for (int i = 0; i < n; i++) {
        cout << emp[i].ename << "\t" << emp[i].age << "\t"
             << emp[i].phn_no << "\t" << emp[i].salary << "\n";
    }
}
// main method
int main(){
    // initialzing to 20
    int n = 20;
    // defining the structure
    struct employee emp[n];
    // iterating and getting data from user
    for (int i = 0; i < n; i++) {
        cout << " Enter the details of " << i+1 << "\n";
        cout << "Enter the name: "; 
        cin >> emp[i].ename;
        cout << "Enter the age: ";
        cin >> emp[i].age;
        cout << "Enter phone number: ";
        cin >> emp[i].phn_no;
        cout << "Enter salary: ";
        cin >> emp[i].salary;
    }
    // function calling
    display(emp, n);
    return 0;
}