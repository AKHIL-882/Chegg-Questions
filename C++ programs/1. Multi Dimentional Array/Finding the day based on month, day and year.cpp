#include <iostream>
#include <string>
using namespace std;
//function prototypes
void getInput(int &month, int &day, int &year);
bool isLeapYear(const int year);
int getCenturyValue(const int year);
int getYearValue(const int year);
int getMonthValue(const int month, const int year);
int dayOfWeek(const int month, const int day, const int year);
enum Months {None, January, February, March, April, May, June, July, August, September, October, November, December};
string weekDays[] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
int main(){
   int month = 0;
   int day = 0;
   int year = 0;
   getInput(month, day, year);
   cout <<day<<"/"<<month<<"/"<<year<<" is a "<<weekDays[dayOfWeek(month, day, year)] <<endl;
   system("pause");
   return 0;
}

bool isLeapYear(const int year){
   if (0 == (year % 400) || (0 == (year % 4) && (year % 100)))
       return true;
   else
       return false;
}
int getCenturyValue(const int year){
   return (2 * (3 - div(year / 100, 4).rem));
}
int getYearValue(const int year){
   int mod = year % 100;
   return (mod + div(mod, 4).quot);
}

int getMonthValue(const int month, const int year){
   switch (month){
   case January:
       if (isLeapYear(year))
           return 6;
   case October:
       return 0;
   case May:
       return 1;
   case August:
       return 2;
   case February:
       if (isLeapYear(year))
           return 2;
   case March:
   case November:
       return 3;
   case June:
       return 4;
   case September:
   case December:
       return 5;
   case April:
   case July:
       return 6;
   default:
       return -1;
   }
}

int dayOfWeek(const int month, const int day, const int year){
   return div(day + getMonthValue(month, year) + getYearValue(year) + getCenturyValue(year), 7).rem;
}

void getInput(int &month, int &day, int &year){
   do{
       cout << "Enter the month (1-12): ";
       cin>>month;
       if(month<0||month>12)
               cout<<"Invalid year"<<endl;

   }while(month<0 || month>12);

   do{
       cout << "Enter the day (1-31): ";
       cin>>day;
       if(day<0|| day>31)
               cout<<"Invalid day"<<endl;

   }while(day<0 || day>31);
       do{

           cout << "Enter the year: ";
           cin>>year;

           if(year<0)
               cout<<"Invalid year"<<endl;
       }while(year<0);

}