#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_set>
   


using namespace std;
string toLowerCAse(const string &input){
    string result;
    result.reserve(input.size());
    for(char c: input){
        result+=tolower(c);
    }
    return result;
}
int main(){
    string word;
    // se crea una lista o set ordenados de datos para alojar datos sin orden especifico, como una bolsa.   
    unordered_set<string> seenWords;
    bool firstWord=true;
    while (cin>> word){
        string lowerWord=toLowerCAse(word);
        if(seenWords.find(lowerWord)!=seenWords.end()){
            cout<< (firstWord ? ".":" .");
        } else{
            cout << (firstWord ? "":" ")<<word;
            seenWords.insert(lowerWord);
        }
        firstWord=false;
    }
    return 0;
}