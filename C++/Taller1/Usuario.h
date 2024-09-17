#pragma once
#include "MaterialBibliografico.h"
#include <iostream>
#define MAX_USUARIO 5
class MaterialBibliografico;
class Usuario
{
private:
    std::string nombre, id;
    MaterialBibliografico *materialesPrestados[MAX_USUARIO];
    int numerosMaterialesEnUso;

public:
    int getNumerosMaterialesEnUso();
    void setNumerosMaterialesEnUso(int numerosMaterialesEnUso_);

    Usuario(std::string nombre_, std::string id_);
    std::string getNombre();
    void setNombre(std::string nombre_);
    std::string getId();
    void setId(std::string id_);
    MaterialBibliografico *getMaterialPrestado(int index);
    void setMaterialPrestado(MaterialBibliografico *material, int index);
    std::string getInfo();
    std::string  toString();
    void prestarMaterial(MaterialBibliografico *material);
    void devolverMaterial(MaterialBibliografico *material);
    void  devolverMateriales();
    std::string getInfoPrestados();
    ~Usuario();
};
