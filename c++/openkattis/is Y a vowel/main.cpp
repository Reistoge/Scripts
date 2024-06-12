// https://open.kattis.com/problems/isyavowel
#include <bits/stdc++.h>
using namespace std;
bool is(char w,string vowels){
    for(char c: vowels){
        if(c== w){
            return true;
        }
    }
    return false;
}
int main(){
    
    string vowels1={"aeiou"};
    string vowels2={"aeiouy"};
    int n=0;
    int n2=0;
    string a;
    cin >> a;
    for(char c : a){
        if(is(c,vowels1)){
            n++;
        }
        if(is(c,vowels2)){
            n2++;
        }
    }
    cout<< n <<" "<<n2;
}