#pragma once
#include <iostream>
#include "MaterialBibliografico.h"
class Libro : public MaterialBibliografico{
    private:
       std::string fechaPublicacion,resumen;
    public:
        Libro(
         std::string titulo_,
         std::string isbn_,
         std::string autor_,
         std::string estado_,
         std::string fechaPublicacion_,
         std::string resumen_
         );
         
        std::string getFechaPublicacion();
        std::string getResumen();
        std::string getInformacion();
        void mostrarInformacion();

};
