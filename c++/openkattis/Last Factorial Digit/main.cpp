#include <iostream>
using namespace std;
int main(){
    int T=0;
    cin >> T;
    int *numbers=new int[T];
    for(int i=0;i<T;i++){
        int number=0;
        int product=1;
        cin >> number;
        
        for(int j=1;j<=number;j++){
            product=product*j;

        }
        numbers[i]=product%10;
        
    }
    
    for(int k=0;k<T;k++){
        cout<<numbers[k]<<endl;
    }

    return 0;
}