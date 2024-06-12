#include <iostream>
#include <string>
#include <map>

using namespace std;
int main(){
    
    int T=0;
    cin >>T;
    int places[100]={0};
    for(int i=0;i<T;i++){
        int T2=0;
        cin >>T2;
        map<string,int> places_frequency;
        for(int j=0;j<T2;j++){
            string place;
            cin >>place;
            places_frequency[place]++;    
        }
        for(auto p: places_frequency){
            places[i]++;
        }
    }
    for(int answer:places){
        if(answer!=0){
            cout<< answer<<endl;
        }
        
    }


    return 0;
}