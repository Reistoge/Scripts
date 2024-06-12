#include <iostream>
using namespace std;
int main(){

    int T=0;

    cin >> T;
    int *N=new int[T];
    
    for(int i=0;i<T;i++){
        cin>>N[i];
    }
    
    for(int j=0; j<T;j++){
        if(N[j]%2==0){
            cout << N[j]<< " is even"<<endl;
        }
        else{
            cout << N[j]<< " is odd"<<endl;
        }

    }
    delete []N;
    return 0;
}