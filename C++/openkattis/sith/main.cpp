#include <iostream>
#include <string>
using namespace std;

int main(){
    string name;
    double a=0;
    double b=0;
    double c=0;
    getline(cin, name);
    cin >>a>>b>>c;
    if(a>b  && c ==abs(a-b)){
        cout<<"VEIT EKKI";
        
    }  
    else if (c !=abs(a-b)){
        cout <<"JEDI";
    }
    else if (c==abs(a-b)&& a>b){
        cout<<"SITH";
    }

    return 0;

}