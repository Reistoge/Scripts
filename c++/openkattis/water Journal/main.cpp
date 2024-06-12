// https://open.kattis.com/problems/waterjournal
#include <bits/stdc++.h>
using namespace std;
bool is(int n, vector<int> arr1){
    for(int i : arr1){
        if(i== n){
            return true;
        }
    }    
    return false;
}
int main(){
    int n,min,max,n4=0;
    cin >> n>> min >>max;
    vector<int> numbers(n-1);
    for(int i =0; i<numbers.size(); i++){
        cin >> numbers[i];
    }
    if(is(min,numbers) && is(max,numbers)){
        for(int i=min; i<=max ;i++){
            cout<< i <<"\n";
        }
    }
    else if(is(min,numbers) && !is(max,numbers)){
        cout<<max;
    } 
    else if(!is(min,numbers) && is(max,numbers)){
        cout <<min;
    }
    else{
        cout<<-1;
    }    
}
