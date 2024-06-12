#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main(){
    int N;
    cin >> N;
    int sum=0;
    string total;
    for(int i=0;i<N;i++){
        string number;
        cin >> number;
        number+="0";
        int rNumber=stoi(number.substr(0,number.length()-2));
        int powd=stoi(number.substr(number.length()-2,number.length()-1));
        powd/=10;
        
        
        sum+=pow(rNumber, powd);

    }
    cout << sum;


    return 0;
}