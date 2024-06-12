#include <iostream>
using namespace std;
int main(){
    float N=0;
    float K=0;
    float sum=0;
    cin >> N>>K;
    for(int i=0;i<K;i++){
        float rating;
        cin >> rating;
        sum+=rating;
    }
    float max=(((N-K)*3)+sum)/N;
    float min=(((N-K)*-3)+sum)/N;
    cout<<min<<" "<<max;



}