#include <iostream>
using namespace std;
int main(){
    int T;
    cin>> T;
    
    // (2+2-1)=3, 3*3
    // (3+3-1)=5, 5*5
    // (5+5-1)=9, 9*9
    //(9+9-1)=17,=17*17
    int N=2;
    
    int k=0;
    for(int i=0;i<T;i++){
        k=N+N-1;
        N=k;    

        
        
    }
    cout << N*N<<endl;
    
   

    return 0;

}