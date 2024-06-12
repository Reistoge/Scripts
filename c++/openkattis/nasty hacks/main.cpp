#include <iostream>
using namespace std;
int main(){
    int N=0;
    cin>> N;
    int *line=new int[N];
    
    for(int i=0;i<N;i++){
        int r=0;
        int e=0;
        int c=0;
        cin >> r>> e>> c;
        if(r==(e-c)){
            line[i]=0;
            // da lo mismo;
        }
        if(r>(e-c)){
            line[i]=-1;
            // se esta ganando sin advertising
        }
        if(r<(e-c)){
            line[i]=1;
            // se esta ganando con advertising
        }

    }
    for(int j=0; j<N;j++){
        
        switch(line[j]) {
            case -1:
                cout <<"do not advertise"<< endl;
                break;

            case 0:
                cout<<"does not matter"<<endl;
                break;

            case 1:
                cout<<"advertise"<<endl;
                break;
        }
    }

    delete[] line;
    return 0;

}