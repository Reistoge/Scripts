#include <bits/stdc++.h>
#include <chrono>

using namespace std;
double fibonacci(double n)
{
    if (n == 0)
    {
        return 0;
    }
    else if (n == 1)
    {
        return 1;
    }
    else
    {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}
// 0 1 2 3 4 5 6 7 8 9 
// 0 1 1 2 3 5 8 13 21
double fibonacci2(int n, double memo[])
{
    double result = 0;

    if (memo[n] >= 1)
    {
        return memo[n];
    }
    if (n <= 2)
    {
        result = 1;
    }

    else
    {
        result = fibonacci2(n - 1, memo) + fibonacci2(n - 2, memo);
    }
    memo[n] = result;
    return result;
}

int main()
{
    int n;
    cin >> n;
    double memo[n];

    clock_t begin = clock();
    cout << fibonacci2(n,memo);
    clock_t end = clock();
    double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
    cout<<"\n"<<elapsed_secs;
    return 0;
}
