// https://open.kattis.com/problems/linesperhour
#include <bits/stdc++.h>
using namespace std;
int main(){
    float minlLimit=300;
    int problems=0;
    float n,lph;
    cin >> n >> lph;
    
    vector <float> v(n);
    for(int i=0; i <v.size();i++){
        cin >>v[i];
    }
    sort(v.begin(),v.end());
    for(int i =0; i<v.size();i ++){
        minlLimit-=(60*v[i])/lph;
        if(minlLimit<0){
            break;
        }
        problems++;

    }
    
    cout<<problems;
    


}