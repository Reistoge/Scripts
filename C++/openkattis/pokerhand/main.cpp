#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main(){
    string Cards,ranks;
    int repeat;
    getline(cin, Cards);
    for(int i=0;i<(Cards.length()-1);i+=3){
        ranks+=Cards[i];
        
    }
    for(int j=0;j<5;j++){
        if (ranks.find_last_of(ranks[j])==j && ranks.find_first_of(ranks[j])==j){
            // no se repite
            ranks[j]=0;

        }

        
    }  
    for(char c:ranks){
        if (c==0){
            
        }
        if(c!=0){
            
            repeat+=1;
        }

    }
    if(repeat==0){
        repeat=1;
    }
    
    
    cout << repeat;
    return 0;
}