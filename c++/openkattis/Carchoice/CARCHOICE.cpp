// resolucion de Problem A CarChoice
#include <iostream>
using namespace std;

int main() {
    float T,x1,x2,y1,y2;
    cin >>T;
    for(int i=0;i<T;i++){
        cin >>x1>>x2>>y1>>y2;
        if((y1/x1)>(y2/x2)){
            cout<<1<<endl;
        }
        else if((y1/x1)<(y2/x2)){
            cout<<-1<<endl;
        }
        else{
            cout<<0<<endl;
        }
    }
    return 0;
}