#include <iostream>
using namespace std;
int main(){
    int width=0;
    int pieces=0;
    int tempArea=0;

    cin >> width>>pieces;

    for(int i=0;i<pieces;i++){
        int tempW=0;
        int tempL=0;
        cin >> tempW>> tempL;
        tempArea+=(tempW*tempL);
            


    }
    cout << (tempArea/width);

}