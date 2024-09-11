#pragma once
#include <iostream>
 
class Impresora{
    public:
        void menu();
        void imprimir(std::string l,bool saltar);
        void showAgregarMaterial();
        void showMostrarInformacion();
        void showBuscarMaterial();
        void showPrestarMaterial();
        void showDevolverMaterial();
        void showGestionUsuarios();
        void showCrearUsuario();
        void showBuscarUsuario();
        void showEliminarUsuario();
        void showVolverMenu();
};