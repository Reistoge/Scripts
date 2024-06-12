#include <iostream>
#include <string>
using namespace std;

int main(){

   string word;
   bool hiss=false;
   cin>>word;
   int i=0;
   while(hiss==false&&i<=word.length()){
        if(word[i-1]!='s'&&word[i]=='s'&& word[i+1]=='s'&& word[i+2]!='s'){
            cout<<"hiss"<<endl;
            hiss=true;

            
        }

        i++;
    }
    if(hiss==false){
        cout<<"no hiss";
    }

    

    
    return 0;
}