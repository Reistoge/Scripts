#include <iostream>
#include <cmath>
#include <iomanip>
 
using namespace std;
int main(){

    int a=0;
    int b=0;
    int c=0;
    int d=0;
    cin >>a>>b>>c>>d;
    double maxArea=0;
    
    maxArea=sqrt((-a+b+c+d)*(a+-b+c+d)*(a+b-c+d)*(a+b+c-d))/4;
    cout << fixed << setprecision(15) << maxArea; 


    return 0;
}