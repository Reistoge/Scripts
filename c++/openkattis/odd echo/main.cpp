#include <iostream>
#include <string>
using namespace std;
// iterando un puntero.
int main(){
    int N;
    cin >> N;
    string *words=new string[N];
    for(int i=0;i<N;i++){
        cin>>words[i];
    }
    for(int j=0;j<N;j+=2){
        cout<<words[j]<< endl;
    }
    delete[] words;
}

