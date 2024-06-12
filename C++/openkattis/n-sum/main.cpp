#include <iostream>
using namespace std;
int main(){

    /* you have to assign the variables to 0 because it will have a weird number value (memory moment) */
    // int T,N,temp; ----> by this, N T or temp could have weird number values. (ask to ignisse)
    int N=0;
    int T=0;
    int temp=0;
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> temp;
        T+=temp;
    }
    cout << T;


    return 0;
}