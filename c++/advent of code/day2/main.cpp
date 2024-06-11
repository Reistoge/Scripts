#include <bits/stdc++.h>
using namespace std;
bool isdigit(char character){
    switch(character){
        case '0':
            return true;
        case '1':
            return true;
        case '2':
            return true;
        case '3':
            return true;
        case '4':
            return true;
        case '5':
            return true;
        case '6':
            return true;
        case '7':
            return true;
        case '8':
            return true;
        case '9':
            return true;
        default:
            return false;
        
    }
    
}
int digit(char character){
    switch(character){
        case '0':
            return 0;
        case '1':
            return 1;
        case '2':
            return 2;
        case '3':
            return 3;
        case '4':
            return 4;
        case '5':
            return 5;
        case '6':
            return 6;
        case '7':
            return 7;
        case '8':
            return 8;
        case '9':
            return 9;
    }
    return 0;
    
}
vector <string> split(string text,char element ){
    string bag;
    vector <string> words;
     
    for(int i=0;i<text.size();i++){
        if(text[i]!=element ){
            bag+=text[i];

        }
        if (text[i+1]==element || i==text.size()-1){
            words.push_back(bag);
            bag="";
        }
        

    }
     
    return words;


}

bool validate(vector<string> game){
    
    int red=0;
    int blue=0;
    int green=0;
    for(int i=0;i<game.size();i++){

        vector<string> Player;
        vector<string> number_and_color;
        Player = split(game[i],',');
        
        for(int i=0;i<Player.size();i++){
            
           
             
            number_and_color=split(Player[i],' ');
            string number=number_and_color[0];
            string color=number_and_color[1];
            
             
            int n=0;

            if (number.size()==1){
                n=digit(number[0]);
            }
            else if(number.size()==2){
                int decimal=digit(number[0])*10;
                int unit=digit(number[1]);
                n=decimal+unit;
            }
            if (color[0]=='r' && n>12){
                 
                return false;
            }
            else if (color[0]=='g'&& n>13){
                 
                return false;
            }
            if (color[0]=='b'&& n>14){
                 
                return false;
            }
            
           
             
            
             
            
            
            

                 

            
        }
        
        
        
         

    }
    return true;
     
     
      
    //only 12 red cubes, 13 green cubes, and 14 blue cubes
     
     

}

int main(){

    string myText;  
    int sum=0;
    int games=1;
    // Read from the text file
    ifstream MyReadFile("input.txt");
    while (getline (MyReadFile, myText)) {
        vector <string> parts=split(myText,':');
        
        
        vector <string> game=split(parts[1],';');
         
        
        
        if(validate(game)){
            sum+=games;
             
             
             
        };
        cout<<"\n";
        games++;

        

       
       /*  vector <string> game=split(parts[1],';');
        for (int i = 0; i < game.size(); i++)
        {
            cout<<parts[i]<<"\n";
        } */
        

        

    }
    cout<<sum;
    return 0;


}