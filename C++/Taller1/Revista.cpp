#include "Revista.h"
Revista::Revista(
         std::string _nombre,
         std::string _isbn,
         std::string _autor,
         bool _estado,
         int _numeroEdicion,
         std::string _mesPublicacion
         ): MaterialBibliografico(
            _nombre,
            _isbn,
            _autor,
            _estado),
            numeroEdicion(_numeroEdicion),
            mesPublicacion(_mesPublicacion) {};
int Revista::getFechaPublicacion(){};
std::string Revista::getMesPublicacion(){};