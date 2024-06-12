#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {
  
  string rank_card;
  map<char,int> frecuencias;
  char letter;
  int repeat;
  for(int i=0;i<5;i++){
    string card;
    cin >> card;
    rank_card+=card[0];
    
   
    }
    for(char c:rank_card){
        if(frecuencias.count(c)>0){
            frecuencias[c]++;
        }
        else{
            frecuencias[c]=1;
        }
    }
    int max_char=0;
    
    for(auto par:frecuencias){
       if(par.second>max_char){
            max_char=par.second;
       }
       
    }
    cout<<max_char;
    

     


  
  
  

  return 0;
}