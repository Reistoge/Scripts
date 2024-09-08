#include "Sistema.h"
#include "Impresora.h"

using namespace std;
int main()
{
    //para compilar debes colocar desde m
    Sistema *sistema = new Sistema();
    Impresora *impr = new Impresora();
    
    string input;
    while (input != "7")
    {
        impr->menu();
        getline(cin, input);
        if (input == "1")
        {
            impr->showAgregarMaterial();
            // tomamos el input del nuevo material
            getline(cin, input);

            if(sistema->agregarMaterial(input)){
                cout <<"Material "<< input<<" fue agregado correctamente" << endl;
            }
            else{
                cout << "No se puede agregar el material " << input << endl;
            }
        }
        else if (input == "2")
        {
            impr->showMostrarInformacion();
        }
        else if (input == "3")
        {
            impr->showBuscarMaterial();
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
