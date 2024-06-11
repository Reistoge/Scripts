#include <bits/stdc++.h>
using namespace std;
// g++ -s -O3 -ftime-report hello.c -o hello.exe

vector<int> check_number_forward(string text){
    vector<int> Numbers(2,0);
    for(int i=0; i<text.size();i++){
        switch (text[i]){
            //afasfdhone
            case 'o':
                if(text[i+1]=='n' && text[i+2]=='e' && (i+3)<=text.size()){
                    Numbers[0]=1;
                    Numbers[1]=i;
                    return  Numbers;
                }
            case 't':
                if(text[i+1]=='w' && text[i+2]=='o' && (i+3)<=text.size()){
                    Numbers[0]=2;
                    Numbers[1]=i;
                    return  Numbers;
                }
                else if(text[i+1]=='h' && text[i+2]=='r' && text[i+3]=='e'&& text[i+3]=='e' && (i+5)<=text.size()){
                    Numbers[0]=3;
                    Numbers[1]=i;
                    return  Numbers;
                }
            case 'f':
                if(text[i+1]=='o' && text[i+2]=='u' && text[i+3]=='r'&& (i+4)<=text.size()){
                    Numbers[0]=4;
                    Numbers[1]=i;
                    return  Numbers;
                }
                else if(text[i+1]=='i' && text[i+2]=='v' && text[i+3]=='e'&& (i+4)<=text.size()){
                    Numbers[0]=5;
                    Numbers[1]=i;
                    return  Numbers;
                }
            case 's':
                if(text[i+1]=='i' && text[i+2]=='x' &&(i+3)<=text.size()){
                    Numbers[0]=6;
                    Numbers[1]=i;
                    return  Numbers;
                }
                else if(text[i+1]=='e' && text[i+2]=='v' && text[i+3]=='e'&& text[i+4]=='n'&& (i+5)<=text.size()){
                    Numbers[0]=7;
                    Numbers[1]=i;
                    return  Numbers;
                }
            case 'e':
                if(text[i+1]=='i' && text[i+2]=='g' &&text[i+3]=='h'&&text[i+4]=='t'&&(i+5)<=text.size()){
                    Numbers[0]=8;
                    Numbers[1]=i;
                    return  Numbers;
                }
            case 'n':
                if(text[i+1]=='i' && text[i+2]=='n' &&text[i+3]=='e' &&(i+4)<=text.size()){
                    Numbers[0]=9;
                    Numbers[1]=i;
                    return  Numbers;
                } 
        }


    }
    Numbers[0]=0;
    Numbers[1]=-1;     
    return Numbers;
}
int main() {
    
    // Create a text string, which is used to output the text file
    string myText;
    cin >> myText;
    vector<int> number_and_pos=check_number_forward(myText);
    // Read from the text file
    
        
    cout<<number_and_pos[0]<<"\n";
    
    // Close the file
    
    return 0;
        
}