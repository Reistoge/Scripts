#include<bits/stdc++.h>
using namespace std;
long long fibonacci(long long n) {
		if(n==0) {
			return 0;
		}
		else if (n==1|| n==2) {
			return 1;
		}
		else {
			return fibonacci(n-1)+fibonacci(n-2);
		}
}
int main(){
    cout<<fibonacci(100);
	return 0;
    

}