#include <bits/stdc++.h>
using namespace std;
// g++ -s -O3 -ftime-report hello.c -o hello.exe
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

vector<int> check_number_forward(string text){
    vector<int> Numbers(2,0);
    for(int i=0; i<text.size();i++){
        switch (text[i]){
             
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
vector<int> check_number_back(string text){
    vector<int> Numbers(2,0);
    for(int i=text.size()-1; i>=0;i--){
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
                if(text[i-1]=='e'&&text[i-2]=='v'&&text[i-3]=='e' && text[i-4]=='s' && i-5>=0){
                    Numbers[0]=7;
                    Numbers[1]=i-4;
                    return Numbers;
                }

            case 't':
                //thgei
                if(text[i-1]=='h'&&text[i-2]=='g'&&text[i-3]=='i' && text[i-4]=='e' && i-5>=0){
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
vector<int> swap(vector <int> lista,int i,int j){
    int aux=lista[i];
    lista[i]=lista[j];
    lista[j]=aux;
    return lista;
    

}
vector<int> delete_element(vector <int> lista,int element){
    int n=0;
    vector <int> not_elements;
    for(int i:lista){
        if(i!=element){
            not_elements.push_back(i);
        }
    }
    return not_elements;

     
    
}
int bubble_sort(vector <int> positions_,vector <int> numbers_){
    vector <int> positions=delete_element(positions_,-1);
    vector <int> numbers=delete_element(numbers_,0);
    int final_number=0;
    for(int i=0;i<positions.size();i++){
        for(int j=i+1;j<positions.size();j++){
            if(positions[i]>positions[j]){
                positions=swap(positions,i,j);
                numbers=swap(numbers,i,j);
            }
        }
    }
    int n=0;
    for(int i: numbers){
        if(numbers[i]!=0){
            n++;
        }

    }
    /* for(int i:numbers){
            cout<<i<<' ';
            
        } 
        cout<<"\n";
        for(int i:positions){
            cout<<i<<' ';
            
        }  */
    return final_number=numbers[0]*10+numbers[numbers.size()-1];
     
    
    
    
    

}

 
   
int main() {
    
    // Create a text string, which is used to output the text file
    string myText;  

    // Read from the text file
    ifstream MyReadFile("input.txt");
    int sum=0;
    // Use a while loop together with the getline() function to read the file line by line
    while (getline (MyReadFile, myText)) {
    // Output the text from the file
        vector<int> Number_and_Pos_forward=check_number_forward(myText);
        int letter_number_forward=0;
        letter_number_forward=Number_and_Pos_forward[0];
        int letter_number_forward_Pos=Number_and_Pos_forward[1];
        
        
        vector<int> Number_and_Pos_back=check_number_back(myText);
        int letter_number_back=0;
        letter_number_back=Number_and_Pos_back[0];
        int letter_number_back_Pos=Number_and_Pos_back[1];


        
        int decimal=0;
        int decimal_pos=-1;
        int unit=0;
        int unit_pos=-1;
        for(int i=0; i<myText.length();i++){

                if(isdigit(myText[i]) ){
                    
                     
                    decimal=digit(myText[i]);
                    decimal_pos=i;
                    
                    break;
                   
                    
                }
        }
        
        for(int i=myText.length(); i>=0;i--){
                if(isdigit(myText[i]) ){
                     
                    unit=digit(myText[i]);
                    unit_pos=i;
                    break;
                }
            
        }
        int final_number=0;
        vector <int> positions={decimal_pos,unit_pos,letter_number_forward_Pos,letter_number_back_Pos};
        vector <int> numbers={decimal,unit,letter_number_forward,letter_number_back};
        if(letter_number_forward_Pos!=-1 && decimal_pos!=-1){
            // cout<<'a'<<"\n";
            final_number=bubble_sort(positions,numbers);
        }
        else if(letter_number_forward_Pos==-1){
            // cout<<'b'<<"\n";
            final_number=decimal*10+unit;
        }
        else if(decimal_pos==-1){
            // cout<<'c'<<"\n";
            final_number=letter_number_forward*10+letter_number_back;
            
        }
        
         
        sum+=final_number;
        /* cout<<final_number<<' '<<sum<<"\n";  */
        

        /* letter_number_forward
        letter_number_forward_Pos
        letter_number_back
        letter_number_back_Pos
        decimal
        decimal_pos
        unit
        unit_pos

        if(decimal_pos<letter_number_back_Pos && decimal_pos!=-1&& letter_number_forward_Pos!=-1 ){
            // 
            // int int word word: decimal*10 + back
            // int word int word: decimal*10 + back
            // int word: (decimal or unit)*10 + (forward or back)
            final_number=decimal*10 + letter_number_back;
        }
        else if(letter_number_forward_Pos<unit_pos && decimal_pos!=-1&& letter_number_forward_Pos!=-1 ){
            // word word int int: forward *10 unit
            // word int word int: forward*10+ unit
            // word int: (forward or back)*10 +(decimal or unit)
            final_number=letter_number_forward_Pos*10+unit;
        }
        else if(decimal_pos<unit_pos)
        {
            if(letter_number_forward_pos!=-1 && letter_number_forward_Pos>decimal){
                // int word word int: decimal*10+ unit
                // int word int: decimal*10 + unit
                final_number=decimal*10+ unit;
            }
            else if(letter_number_forward_pos==-1){
                // if forward pos ==-1 back_pos also is -1

                // int int int: decimal*10 + unit
                // int int: decimal*10 + unit
                final_number=decimal*10 + unit;
            }

            

        }
        else if(letter_number_forward_Pos<letter_number_back_Pos){
            final_number=letter_number_forward*10+letter_number_back;
        }
        else if()

 */

        // combinatory cases: 
        

        
 

         

        // rare cases:
         
        // int: (decimal or unit)*10 + (decimal or unit)
        // word: (forward or back) + (back or forward)

        

        





        /* if (letter_number_forward_Pos!=-1 ){
            if(unit_pos!=decimal_pos){
                if(letter_number_forward_Pos<decimal_pos){
                    cout<<"case 1"<<"\n";
                    final_number=(letter_number_forward*10)+decimal;
                    sum+=final_number;

                }
                else if(letter_number_forward_Pos>decimal_pos && unit_pos>letter_number_forward_Pos){
                    final_number=(decimal*10)+unit;
                    cout<<"case 2"<<"\n";
                    sum+=final_number;
                }
                else if(letter_number_forward_Pos>decimal_pos && unit_pos<letter_number_forward_Pos){
                    cout<<"case 3"<<"\n";
                    final_number=(unit*10)+letter_number_forward;
                    sum+=final_number;
                }
            }
            else if(decimal_pos==unit_pos){
                if(letter_number_forward_Pos>decimal_pos){
                    cout<<"case 4"<<"\n";
                    final_number=(decimal*10)+letter_number_forward;
                    sum+=final_number;
                }
                else if(letter_number_forward_Pos<decimal_pos){
                    cout<<"case 5"<<"\n";
                    final_number=(letter_number_forward*10)+decimal;
                    sum+=final_number;
                }

            }
            

        
        } */
        
        /* else if(letter_number_forward_Pos==-1){
            cout<<"case 6"<<"\n";
            final_number=(decimal*10)+unit;
            sum+=final_number;

        } */


         
 
        
       
    }
    cout<<sum;
    // Close the file
    MyReadFile.close();
    return 0;
        
}