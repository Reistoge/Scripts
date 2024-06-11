#include <bits/stdc++.h>
using namespace std;
vector<int> check_number_back(string text){
    vector<int> Numbers(2,0);
    for(int i=text.size(); i>=0;i--){
        switch (text[i]){
            case 'e':
                //eno
                if(text[i-1]=='n' && text[i-2]=='o' && i-3>=0){
                    Numbers[0]=1;
                    Numbers[1]=i-2;
                    return Numbers;

                }
                 
                //eerht
                else if(text[i-1]=='e' && text[i-2]=='r' && text[i-3]=='h'&&text[i-4]=='t'&& i-5>=0){
                    Numbers[0]=3;
                    Numbers[1]=i-4;
                    return Numbers;
                }
                //evif
                else if(text[i-1]=='v' &&text[i-2]=='i' && text[i-3]=='f' && i-4>=0){
                    Numbers[0]=5;
                    Numbers[1]=i-3;
                    return Numbers;
                }
                //enin
                else if(text[i-1]=='n'&& text[i-2]=='i' && text[i-3]=='n' && i-4>=0){
                    Numbers[0]=9;
                    Numbers[1]=i-3;
                    return Numbers;
                }

            case 'o':
                //owt
                if(text[i-1]=='w' && text[i-2]=='t' && i-3>=0){
                    Numbers[0]=2;
                    Numbers[1]=i-2;
                    return Numbers;
                }
            case 'r':
                //ruof
                if(text[i-1]=='u'&&text[i-2]=='o' && text[i-3]=='f' && i-4>=0){
                    Numbers[0]=4;
                    Numbers[1]=i-3;
                    return Numbers;
                }
            case 'x':
                //xis
                if(text[i-1]=='i' && text[i-2]=='s' && i-3>=0){
                    Numbers[0]=6;
                    Numbers[1]=i-2;
                    return Numbers;
                }
            case 'n':
                //seven
                //neves
                if(text[i-3]=='e'&&text[i-3]=='v'&&text[i-3]=='e' && text[i-4]=='s' && i-5>=0){
                    Numbers[0]=7;
                    Numbers[1]=i-4;
                    return Numbers;
                }

            case 't':
                //thgei
                if(text[i-3]=='h'&&text[i-3]=='g'&&text[i-3]=='i' && text[i-4]=='e' && i-5>=0){
                    Numbers[0]=8;
                    Numbers[1]=i-4;
                    return Numbers;
                }


             
            
        }


    }
    Numbers[0]=0;
    Numbers[1]=-1;     
    return Numbers;
}

 
string word="onefourfivesisx";
int main(){

        vector<int> Number_and_Pos_back=check_number_back(word);
        int letter_number_back=0;
        int letter_number_back_Pos=Number_and_Pos_back[1];
        letter_number_back=Number_and_Pos_back[0];

        cout<<letter_number_back<<"\n";
        cout<<letter_number_back_Pos;
         
    
     
    return 0;
}