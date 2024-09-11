 
#include "Sistema.h"
#include "Impresora.h"

using namespace std;
int main()
{
    //para compilar debes colocar desde m
    Sistema *sistema = new Sistema();
    Impresora *impr = new Impresora();
    
    string input;
    bool repetir=false;
    while (input != "7")
    {
        impr->menu();
        if(repetir==false){
            getline(cin, input);

        }
        if (input == "1")
        {
            impr->showAgregarMaterial();
            // tomamos el input del nuevo material
            getline(cin, input);
            if(sistema->agregarMaterial(input)){
                cout <<"Material "<< input<<"\nfue agregado correctamente" << endl;
                 

                
            }
            else{
                cout << "No se puede agregar el material " << input << endl;
            }
            cout << "desea agregar otro material? (si / no)" << endl;
            getline(cin, input);
            cout <<input<<endl;
            if(input=="si"){
                repetir=true;
                input="1";
            }
            else{
                repetir=false;
                input="";
            }

            


            
        }
        else if (input == "2")
        {
            impr->showMostrarInformacion();
            sistema->mostrarInfoMateriales();
        }
        else if (input == "3")
        {

            impr->showBuscarMaterial();
            getline(cin, input);
            if(sistema->buscarMaterial(input)==false){
                cout << "El material " << input << " no existe en el sistema." << endl;

            }

            cout << "desea buscar otro material? (si / no)" << endl;
            getline(cin, input);
            cout <<input<<endl;
            if(input=="si"){
                repetir=true;
                input="3";
            }
            else{
                repetir=false;
                input="";
            }
            
 
            

        }
        else if (input == "4")
        {
            impr->showPrestarMaterial();
            
           
             
        }
        else if (input == "5")
        {
            impr->showDevolverMaterial();
        }
        else if (input == "6")
        {
            impr->showGestionUsuarios();
        }
    }

    delete impr;
    delete sistema;
    return 0;
}
