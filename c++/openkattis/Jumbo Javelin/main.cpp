#include <iostream>
using namespace std;
int main(){
    
    int N=0;
    int total=0;
    cin >> N;
    for(int i=0; i<N;i++){
        int temp;
        cin >> temp;
        total+=temp;

    }
    cout<< total-(N-1);
    // se le va a restar n veces excepto la primera vez ya que la primera vez no se combina.
    return 0;
}