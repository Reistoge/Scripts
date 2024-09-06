#pragma once
#include <iostream>
#include "MaterialBibliografico.h"
class Revista: public MaterialBibliografico {
    private:
        int numeroEdicion;
        std::string mesPublicacion;
    public:
        Revista(
         std::string _nombre,
         std::string _isbn,
         std::string _autor,
         bool _estado,
         int _numeroEdicion,
         std::string _mesPublicacion
         );

        int getFechaPublicacion();
        std::string getMesPublicacion();
        
};