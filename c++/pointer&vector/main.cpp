#include <iostream>
#include <vector>
using namespace std;


int main()
{
    // recorriendo e inicializando un vector
    int n=0;
    cin >> n;
    vector<int> vector1(n,0) ;
    
    for(int i=0; i<vector1.size();i++){
        cout<<vector1[i];
        if(i==n-1){
            cout<<vector1[i]<<endl;

        }
        
    }
    
    //utilizando puntero
    int *p=new int[n];
    
    for(int i=0; i<n-1; i++){
        p[i]+=1;
        cout<<p[i];
    }
    
    delete[] p;
    return 0;
    
}