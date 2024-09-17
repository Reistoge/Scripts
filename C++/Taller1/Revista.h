#pragma once
#include <iostream>
#include "MaterialBibliografico.h"
class Revista : public MaterialBibliografico
{
private:
    int numeroEdicion;
    std::string mesPublicacion;

public:
    Revista(
        std::string titulo_,
       std::string isbn_,
       std::string autor_,
       std::string estado_,
       int numeroEdicion_,
       std::string mesPublicacion_);

    int getNumeroEdicion();
    std::string getMesPublicacion();
    void setNumeroEdicion(int value) ; 
    void setMesPublicacion(std::string value);
    void mostrarInformacion();
    std::string   getInformacion();
    std::string toString();

};