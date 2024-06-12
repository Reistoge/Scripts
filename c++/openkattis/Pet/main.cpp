#include <iostream>
using namespace std;
int main(){
    int max_sum=0;
    int max_index=0;
    int index=0;
    for(int i=0;i<5;i++){
        
        int sum=0;
        int N=0;
        for(int j=0;j<4;j++){
            
            cin >> N;
            sum+=N;
            
            
        }

        if(sum>max_sum){
            max_sum=sum;
            max_index=i+1;
        }
        

    }
    cout<<max_index<<" "<<max_sum<<endl;



    return 0;
}