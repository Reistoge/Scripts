#include <iostream>
#include <string>
#include <map>
using namespace std;

int main() {
  // create a map to store the frequency of each rank
  map<char, int> freq;
  // read the input and update the frequency map
  for (int i = 0; i < 5; i++) {
    string card;
    cin >> card;
    char rank = card[0];    
    freq[rank]++;
  }
  // find the maximum frequency among all ranks
  int max_freq = 0;
  for (auto p : freq) {
    max_freq = max(max_freq, p.second);
  }
  // output the maximum frequency as the strength of the hand
  cout << max_freq << endl;
  return 0;
}
