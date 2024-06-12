//https://open.kattis.com/problems/npuzzle
#include <vector>
#include <iostream>
using namespace std;

vector<vector<int>>position={{0,0},{0,1},{0,2},{0,3},
                                 {1,0},{1,1},{1,2},{1,3},
                                 {2,0},{2,1},{2,2},{2,3},
                                 {3,0},{3,1},{3,2},{3,3}};


vector<int> getPositionWithLetter(char letter){
    switch ( letter){
        case 'A':
            return position[0];
        case 'B':
            return position[1];
        case 'C':
            return position[2];
        case 'D':
            return position[3];
        case 'E':
            return position[4];
        case 'F':
            return position[5];
        case 'G':
            return position[6];
        case 'H':
            return position[7];
        case 'I':
            return position[8];
        case 'J':
            return position[9];
        case 'K':
            return position[10];
        case 'L':
            return position[11];
        case 'M':
            return position[12];
        case 'N':
            return position[13];
        case 'O':
            return position[14];
        case '.':
            return position[15]; 
    }
    return position[0];
}

int main(){

    vector<char> puzzle(15,0);
    int sum=0;
    // create a matrix, put the char in each thing and then with the index calculate the distance between the other matrix
    for(int i=0;i<16;i++){
        cin>>puzzle[i];
    }
    for(int i=0;i<16;i++){
        if (puzzle[i]!='.'){
            vector<int> current_pos=getPositionWithLetter(puzzle[i]);
            vector<int> original_pos=position[i];

            int pos=abs(current_pos[1]-original_pos[1])+abs(current_pos[0]-original_pos[0]);
            sum+=pos;
        }
    }
    cout <<sum;



    


    return 0;
}
