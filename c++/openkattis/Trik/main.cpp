#include <iostream>
#include <string>
using namespace std;

// create a function that finds a number in the array
int findBall(int arr[], int len, int seek) {
  for (int i = 0; i < len; ++i) {
    if (arr[i] == seek) return i;

  }
    return 0;
  
}


int main(){
    int variable[3] = {1, 0, 0};
    
    string line;
    cin >>  line;
    
    
    for(int j=0;j<line.length();j++){
        string c;
        c=line[j];
        size_t findA=c.find("A");
        size_t findB=c.find("B");
        size_t findC=c.find("C");
        if(findA!=-1){
            
            switch (findBall(variable,3,1)){
                case 0:
                    variable[0]=0;
                    variable[1]=1;
                    break;
                

                case 1:
                    variable[1]=0;
                    variable[0]=1;
                    break;
                case 2:
                    variable[2]=variable[2];
                    break;
                
            }   
        };
        if(findB!=-1){
            
            switch (findBall(variable,3,1)){
                case 0:
                    variable[0]=variable[0];
                    break;
                case 1:
                    variable[1]=0;
                    variable[2]=1;
                    break;

                case 2:
                    variable[2]=0;
                    variable[1]=1;
                    break;
                
            }
        };
        if(findC!=-1){
            
            switch (findBall(variable,3,1)){
                case 0:
                    variable[0]=0;
                    variable[2]=1;
                    break;

                case 1:
                    variable[1]=variable[1];
                    break;
                case 2:
                    variable[2]=0;
                    variable[0]=1;
                    break;
            }
            
        };
        
        

    }
    
    cout << (findBall(variable,3,1)+1);
    return 0;
    
}