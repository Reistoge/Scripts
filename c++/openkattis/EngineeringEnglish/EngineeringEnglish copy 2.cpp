#include <iostream>
#include <string>
#include <cctype>

using namespace std;

bool in_array(string value, string *array, int length){
    for (int i = 0; i < length; i++){
        if (value == array[i]){
            return true;
        }
    }

    return false;
}

string toLowerCase(string input){
    string result;
    for (char c : input){
        result += tolower(c);
    }
    return result;
}

int main(){
    string lista[20000];
    int largoLista = 0;
    string word;
    while (cin >> word){
        word = toLowerCase(word);
        if (!in_array(word, lista, largoLista)){
            lista[largoLista] = word;
            largoLista++;
            cout << word << " ";
        }
        else{
            cout << ". ";
        }
    }
    return 0;
}