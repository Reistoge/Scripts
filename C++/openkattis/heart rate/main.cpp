#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
int main(){
    int N;
    cin >> N;
    float B=0;
    float P=0;
    float *answer=new float[N];
    float *b=new float[N];

    for(int i=0; i<N;i++){
        cin >>B;
        cin >> P;
        float BPM=(60*B)/P;
        answer[i]=BPM;
        b[i]=BPM/B;
        
    }
    for(int j=0;j<N;j++){
        cout<<fixed << setprecision(4) << answer[j]- b[j]<<" "<<answer[j]<<" "<<answer[j] + b[j]<<endl;
    }
    delete[] answer;
    delete[] b;
    return 0;
}