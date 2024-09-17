 
#include "Revista.h"
Revista::Revista(
         std::string _titulo,
         std::string _isbn,
         std::string _autor,
         std::string _estado,
         int _numeroEdicion,
         std::string _mesPublicacion
         ) : MaterialBibliografico(
            _titulo,
            _isbn,
            _autor,
            _estado), 
         numeroEdicion(_numeroEdicion),
         mesPublicacion(_mesPublicacion) {this->tipo="Revista";};
int Revista::getNumeroEdicion(){return this-> numeroEdicion;};
std::string Revista::getMesPublicacion(){return this->mesPublicacion;};
void Revista::setNumeroEdicion(int value){this->numeroEdicion =value;};
void Revista::setMesPublicacion(std::string value){this->mesPublicacion = value;}
void Revista:: mostrarInformacion(){
   MaterialBibliografico::mostrarInformacion();
   std::cout << "Numero Edicion: "<<this->getNumeroEdicion()<<std::endl;
   std::cout <<"Mes de publicacion: "<< this-> getMesPublicacion() << std::endl; 
};
std::string  Revista:: getInformacion(){
   std::string info = MaterialBibliografico::getInformacion();
   info += "\nNumero de edicion: " + std::to_string(numeroEdicion) + "\nMes de publicacion: " +mesPublicacion;
   return info;
 
};
std::string Revista::toString(){
   return MaterialBibliografico::toString()+";"+std::to_string(numeroEdicion)+";"+mesPublicacion;
}