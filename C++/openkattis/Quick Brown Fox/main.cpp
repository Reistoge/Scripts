https://open.kattis.com/problems/quickbrownfox
#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;
string isPangram(string alphabet, string p ){
    string missing="";
    // formateamos a minuscula todo el string.
    for (auto& x : p) { 
            x = tolower(x); 
        }
    for(char c : alphabet){
    //                   que es esto
        if (p.find(c) != string::npos || c==' ')
        {
            // encontrado!!
            continue;
        }
        else
        {
             
           missing+=c; // guardamos el char que falta.
        }
    }
    return missing;
    
}
int main()
{
    // bruh
    string alphabet = {"abcdefghijklmnopqrstuvwxyz"};
    vector<string> respuesta;
    int n;
    cin >> n;
    cin.ignore(); // error raro de getline
    
    while(n>0){
        
        string p="";
         
        getline(cin,p); // guardamos linea
        string out=isPangram(alphabet,p);
        
        if(out==""){

            respuesta.push_back("pangram");
        }
        else{
           respuesta.push_back("missing "+out);
        }
        n--;
        
        
    }
 
    //mostramos las respuestas
    for(string s : respuesta){
        cout<<s<<"\n";
    }
    return 0;
   
    
}