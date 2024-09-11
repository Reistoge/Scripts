
#include "MaterialBibliografico.h"
MaterialBibliografico::MaterialBibliografico(std::string n, std::string i, std::string a, std::string e) : titulo(n), isbn(i), autor(a), isPrestado(e) {}
void MaterialBibliografico::mostrarInformacion()
{
    // std::string nombre,isbn,autor;
    std::cout << "Nombre: " << this->getTitulo() << std::endl;
    std::cout << "ISBN: " << this->getIsbn() << std::endl;
    std::cout << "Autor: " << this->getAutor() << std::endl;
    if (this->getIsPrestado() != "disponible")
    {
        std::cout << "Estado: disponible" << std::endl;
    }
    else
    {

        std::cout << "Estado: prestado" << std::endl;
        std::cout << "Id del usuario " << usuarioDelMaterial->getId() << std::endl;
    }
};
std::string MaterialBibliografico::getInformacion()
{
    std::string response="";
    // std::string nombre,isbn,autor;
    response+= "Nombre: " + this->getTitulo()+"\nISBN: " +  this->getIsbn() +"\nAutor: " + this->getAutor();
 
    if (this->getIsPrestado() != "disponible")
    {
        response+= "\nEstado: disponible";
        return response;
    }
    else
    {

          response+="\nEstado: prestado\nId del usuario: " + this->usuarioDelMaterial->getId();
          return response;

        
    }
}
std::string MaterialBibliografico::getTitulo() { return this->titulo; };
void MaterialBibliografico::setTitulo(std::string value) { this->titulo = value; };
std::string MaterialBibliografico::getIsbn() { return this->isbn; };
void MaterialBibliografico::setIsbn(std::string value) { this->isbn = value; };
std::string MaterialBibliografico::getAutor() { return this->autor; };
void MaterialBibliografico::setAutor(std::string value) { this->autor = value; };
std::string MaterialBibliografico ::getIsPrestado() { return this->isPrestado; };
void MaterialBibliografico::setIsPrestado(std::string value) { this->isPrestado = value; };