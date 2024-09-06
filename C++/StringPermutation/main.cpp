// recursion to find the number of strings in a character combination
#include <iostream>
#include <bits/stdc++.h>

using namespace std;
void permu(string a){
//    string characters="abcdefghijklmnoprstuvwxyz1234567890";
    string characters="abc";
    if(a.length()==3){
       cout<<a<<"\n";
    }
    else{
        for(char c : characters){
            permu(a+c);
             
        }
    }
}
int main()
{   
    permu("");
}