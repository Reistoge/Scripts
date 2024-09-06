#ifndef MATERIAL_BIBLIOGRAFICO_H
#define MATERIAL_BIBLIOGRAFICO_H
//#include <bits/stdc++.h>
#include "Usuario.h"
class Sistema{
    private:
        MaterialBibliografico* biblioteca[100]; 
        Usuario* usuarios[100];
    public:
        bool agregarMaterial(std::string);
        void mostrarInfoMateriales();
        void buscarMaterial();
        void prestarMaterial();
        void devolverMaterial();
        void guardarDatos();
        void leerDatos();
        ~Sistema();

};
#endif