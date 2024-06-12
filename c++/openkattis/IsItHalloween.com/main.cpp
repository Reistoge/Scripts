#include <iostream>
#include <string>

using namespace std;
int main(){
    string month;
    int day;
    string Months[12]={"JAN","FEB","MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV","DEC"};
    
 
        cin >> month >> day;
        
        if(Months[9]==month && day==31||Months[11]==month && day==25){
            cout<<"yup"<<endl;

        }
        else{
            cout<<"nope"<<endl;
        }
        


    return 0;
} 