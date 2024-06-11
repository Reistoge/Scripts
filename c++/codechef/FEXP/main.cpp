// https://www.codechef.com/problems/FEXP
#include <iostream>
using namespace std;

const int MOD = 1e9 + 7;

long long a_to_n(long long a, long long n) {

    
    if (n == 0)
        return 1; // 0¹ = 1
    else if (n == 1)
        return a % MOD; // a¹ = a

    a %= MOD; // Para evitar desbordamiento
    if (n % 2 == 0) {
        long long temp = a_to_n(a, n / 2);
        return (temp * temp) % MOD;
    } else {
        long long temp = a_to_n(a, (n - 1) / 2);
        return (((temp * temp) % MOD) * a) % MOD;
    }
}

int main() {
    int T;
    cin >> T;

    while (T--) {
        long long a, n;
        cin >> a >> n;
        cout << a_to_n(a, n) << endl;
    }

    return 0;
}