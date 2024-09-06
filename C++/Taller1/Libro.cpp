#include "Libro.h"
Libro::Libro(
         std::string _nombre,
         std::string _isbn,
         std::string _autor,
         bool _estado,
         std::string _fechaPublicacion,
         std::string _resumen
         ): MaterialBibliografico(
            _nombre,
            _isbn,
            _autor,
            _estado), 
            fechaPublicacion(_fechaPublicacion),
            resumen(_resumen){};
std::string Libro:: getFechaPublicacion() {};
std::string Libro::getResumen(){};
    
 