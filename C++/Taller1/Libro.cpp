
#include "Libro.h"
Libro::Libro(
    std::string _titulo,
    std::string _isbn,
    std::string _autor,
    std::string _estado,
    std::string _fechaPublicacion,
    std::string _resumen) : MaterialBibliografico(_titulo, _isbn, _autor, _estado), fechaPublicacion(_fechaPublicacion), resumen(_resumen) {

                            };

std::string Libro::getFechaPublicacion() { return fechaPublicacion; };
std::string Libro::getResumen() { return resumen; };
void Libro::mostrarInformacion()
{
   MaterialBibliografico::mostrarInformacion();
   std::cout << "Fecha de publicacion: " << fechaPublicacion << std::endl;
   std::cout << "Resumen: " << resumen << std::endl;
};
std::string Libro::getInformacion()
{
   std::string info = MaterialBibliografico::getInformacion();
   info += "\nFecha de publicacion: " + fechaPublicacion +"\nMes de publicacion: " + resumen;
   return info;
};
