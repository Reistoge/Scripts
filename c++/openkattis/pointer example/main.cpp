#include <iostream>
#include <string>
using namespace std;
 
int main(){
    int N,B;
    cin >> N;
    string *p=new string[N];
    for(int i=0;i<N;i++){
        
        cin >>p[i];
        cout << p[i]<<endl;
    }
    delete[] p;
    

    return 0;
}