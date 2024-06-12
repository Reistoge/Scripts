#include <iostream>
#include <string>
using namespace std;

int main(){

    string word;
    
    cin >> word;
   
    
    if( word.find_last_of("s")==word.find_first_of("s")+1 || word[word.find_last_of("s")]==word[word.find_last_of("s")-1] && word.find_first_of("s")<=word.length()+1 && word.find_last_of("s")<=word.length()+1){
        cout<<"hiss";
    }

    else{
        cout<<"no hiss";
    }

    
    return 0;
}