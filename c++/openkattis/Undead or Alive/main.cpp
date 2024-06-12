#include <iostream>
#include <string>
using namespace std;
int main () {
  string input; // declare a string variable to store the input
  
  getline(cin, input); // read a line of input and store it in input
  //getline is for get an entire line of input, and store it in a string variable.

  size_t smiley = input.find(":)"); // find the index of the first smiley face in the input, or -1 if not found
  size_t frowny = input.find(":("); // find the index of the first frowny face in the input, or -1 if not found
  // size_t is used for store variables that can be unsigned data if :( is not find the variable will be assigned to a giant number (memory issue)
  // in this case size_t takes that value and assign to -1.
  // if has a value=right 
  // if not =-1.
  if (smiley != -1 && frowny == -1) { // if there is a smiley face and no frowny face[^1^][1]
    cout << "alive" << endl; // output alive
  } else if (smiley == -1 && frowny != -1) { // if there is a frowny face and no smiley face
    cout << "undead" << endl; // output undead
  } else if (smiley != -1 && frowny != -1) { // if there are both smiley and frowny faces
    cout << "double agent" << endl; // output double agent
  } else { // if there are no smiley or frowny faces[^1^][1]
    cout << "machine" << endl; // output machine
  }
  return 0;
}