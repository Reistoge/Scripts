#include "MaterialBibliografico.h"
MaterialBibliografico::MaterialBibliografico(std::string n, std::string i,std::string a,bool e): nombre(n), isbn(i), autor(a),estado(e) {}
void MaterialBibliografico::mostrarInformacion(){};
std::string MaterialBibliografico:: getNombre(){return this->nombre;};
void MaterialBibliografico::setNombre(std::string value){this->nombre=value;};
std::string MaterialBibliografico::getIsbn(){return this->isbn;};
void MaterialBibliografico::setIsbn(std::string value){this->isbn=value;};
std::string MaterialBibliografico::getAutor(){return this->autor;};
void MaterialBibliografico::setAutor(std::string value){this->autor=value;};
bool MaterialBibliografico :: getEstado(){return this->estado;};
void MaterialBibliografico:: setEstado(bool value){this->estado=value;};