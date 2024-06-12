#include <iostream>
using namespace std;

int main(){
    int X,Y;
    cin >> X >> Y;
    if(X<0&&Y<0){
        cout<<3;
    }
    else if(X>0&&Y>0){
        cout<<1;
    }
    else if(X<0&&Y>0){
        cout<<2;
    }
    if(X>0&&Y<0){
        cout<<4;
    }
    return 0;

}