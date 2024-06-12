// eye of sauron 
// https://open.kattis.com/problems/eyeofsauron
#include <iostream>
#include <bits/stdc++.h>
// 
using namespace std;
bool checkString(string s){
    int k=s.length()/2;
    if(s.length()%2==0 && s[k-1]=='(' && s[k]==')'){
        return true;

    }
    else{
        return false;
    }
    // if string.size %2 == 0 and string[midle-1]=='(  string[midle]==')

    

}
int main(){
        
    string s;
    cin >> s;
    if(checkString(s)){
        cout<<"correct";
    }
    else{
        cout<<"fix";
    }
    
     
    return 0;
    


    
}
