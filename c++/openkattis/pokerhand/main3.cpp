#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
  // create an array to store the frequency of each rank
  int freq[13] = {0};
  // read the input and update the frequency array
  for (int i = 0; i < 5; i++) {
    string card;
    cin >> card;
    char rank = card[0];
    // convert the rank to an index from 0 to 12
    int index;
    if (rank >= '2' && rank <= '9') {
      index = rank - '2';
    } else if (rank == 'T') {
      index = 8;
    } else if (rank == 'J') {
      index = 9;
    } else if (rank == 'Q') {
      index = 10;
    } else if (rank == 'K') {
      index = 11;
    } else if (rank == 'A') {
      index = 12;
    }
    freq[index]++;
  }
  // find the maximum frequency among all ranks
  int max_freq = *max_element(freq, freq + 13);
  // output the maximum frequency as the strength of the hand
  cout << max_freq << endl;
  return 0;
}
