#include <iostream>
using namespace std;
int main(){
    int H,M;
    while(cin >> H>>M){
        if(M>=45){
        if((M-45)>=10){
            cout <<H<<" "<<(M-45)<<endl;
        }
        if((M-45)<10){
            cout << H<<" "<<(M-45)<<endl;
        }
        
        }
    
        if(M<45){
        if(H-1<0){
            cout<<(H+24)-1<<" "<<(60+M)-45<<endl;
        }
        else{
            cout<<(H-1)<<" "<<(60+M)-45<<endl;    
        }
        

        }


    };
    return 0;
}    
    