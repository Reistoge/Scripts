#pragma once
#include <iostream>
#include "MaterialBibliografico.h"
class Libro : public MaterialBibliografico{
    private:
       std::string fechaPublicacion,resumen;
    public:
        Libro(
         std::string _nombre,
         std::string _isbn,
         std::string _autor,
         bool _estado,
         std::string _fechaPublicacion,
         std::string _resumen
         );
         
        std::string getFechaPublicacion();
        std::string getResumen();

};
