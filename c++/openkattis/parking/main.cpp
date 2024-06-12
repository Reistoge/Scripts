// https://open.kattis.com/problems/parking2
#include <iostream>
#include <bits/stdc++.h>

using namespace std;
vector<int> sort(vector<int> v)
{
    int n = v.size();

    for (int i = 0; i < n; i++)
    {

        for (int j = i + 1; j < n; j++)
        {

            if (v[i] >= v[j])
            {
                int temp = v[i];
                v[i] = v[j];
                v[j] = temp;
            }
        }
    }
    return v;
}
int main()
{
    int t = 0;
    cin >> t;
    while (t > 0)
    {
        vector<int> distances;
        int n = 0;
        int result = 0;
        cin >> n;
        for (int i = 0; i < n; i++)
        {
            int d = 0;
            cin >> d;
            distances.push_back(d);
        }
        distances = sort(distances);
        for (int i = n - 1; i > 0; i--)
        {
            result += abs(distances[i] - distances[i - 1]);
        }
        cout << result + abs(distances[0] - distances[n - 1]) << "\n";

        t--;
    }

    return 0;
}
