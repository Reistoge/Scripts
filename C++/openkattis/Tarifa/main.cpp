#include <iostream>
using namespace std;
int main(){
    int limit=0;
    int months=0;
    int rest=0;
    cin >> limit>>months;
    int temp=limit;
    for(int i=0;i<months;i++){
        limit=temp;
        int spent;
        cin >>spent;
        rest+=limit-spent;

        
    
    }
    cout<< rest+temp;


    return 0;
}