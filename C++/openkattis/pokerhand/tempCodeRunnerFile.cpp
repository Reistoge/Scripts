#include <iostream>
#include <string>
using namespace std;
int main(){
    string Cards,ranks;
    int repeat;
    getline(cin, Cards);
    for(int i=0;i<(Cards.length()-1);i+=3){
        ranks+=Cards[i];
    }
    for(int j=0;j<(ranks.length()-1);j++){
        if(ranks[j]==ranks[j+1]){
            repeat++;
        }
    }
    cout << repeat+1;



    return 0;
}