#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
int main(){

    string word;
    cin >> word;
    int possibility=0;
    //int possibility; ---> WRONG
    // YOU HAVE TO INITIALIAZE THE VARIABLE YOU STUUUPID

    for(char c:word){
        if(word.find_last_of(c)!=word.find_first_of(c)){
            possibility--;
        }
        
    }
    if(possibility<0){
        cout<<0<<endl;
    }
    else{
        cout<<1<<endl;
    }


    return 0;

}