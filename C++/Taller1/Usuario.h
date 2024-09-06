#ifndef USUARIO_H
#define USUARIO_H
#include "MaterialBibliografico.h"
#include <iostream>
class Usuario{
    private:
        std::string nombre,id;
        MaterialBibliografico* materialesPrestados[5];
    public:
        void prestarMaterial();
        void devolverMaterial();
        void mostrarMaterialesPrestados();


};
#endif