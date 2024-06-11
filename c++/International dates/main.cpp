#include <iostream>
#include <string>
using namespace std;

int main(){
    string date;

    cin >> date;

    string day=date.substr(0,2);
    string month=date.substr(3,2); // wtf
    string year=date.substr(6);
    
    if(stoi(month)>12 && stoi(day)<12){
        cout<<"US";
        
    }
    else if(stoi(month)<12 && stoi(day)>12){
        cout<<"EU";

    }
    else if(stoi(month)<12 && stoi(day)<12){
        cout<<"either";
    }

    return 0;
}