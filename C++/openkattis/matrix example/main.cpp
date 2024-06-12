#include <iostream>
using namespace std;
int main(){
    int N;
    cin >> N;
    int **p= new int*[N]; 
    for(int i; i<N;i++){
        p[i]=new int[N];

        for(int j;j<N;j++){
            cin >>p[i][j];
        }
    }
    cout << p[N][N];
    delete[] p;
    return 0;
}