#include <iostream>
 
using namespace std;
 
int main(){
    int N;
    cin >> N;
    float product;
    for(int i=0; i<N;i++){
        float q,y;
        cin >>q>>y;
        product+=q*y;
    }
    cout << product;
    

    return 0;
}