    #include <iostream>
    #include <string>

    using namespace std;

    int main(){
        // Get the input
        string encoding;
        // PpIiKkAaCcHhUu
        // 001=P 002=p 003=3 y asi.

        // nos entregan el cifrado, que seria nuestro abecedario a interpretar
        getline(cin,encoding);

        string msg;
        //  001004006008010012014
        // nos entregan el mensaje que hay que descifrar con el abecedario
        getline(cin, msg);

        string number;


        for(int i = 0; i < msg.length(); i+=3){
            //  partimos el mensaje cada 3 letras
            // i=0
            number = msg.substr(i, 3);
            //number = msg.substr(0,3)
            //number="001"

            cout << encoding[stoi(number)-1];
            // encoding[stoi("001")-1]
            //encoding[1-1]
            //encoding[1]=P
            
            // stoi significa "string to int"
        }

        return 0;
    }