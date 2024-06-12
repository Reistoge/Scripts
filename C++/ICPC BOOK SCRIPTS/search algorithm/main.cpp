#include <iostream>
#include <bits/stdc++.h>
#include <vector>
using namespace std;
vector<int> subset;

void search(int k) {
    if (k == 3+1) {
        
        // process subset
    } else {
        // include k in the subset
        subset.push_back(k);
        search(k+1);
        subset.pop_back();
        // don’t include k in the subset
        search(k+1);
}
}

int main(){


    search(4);



}