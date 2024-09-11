
#include "Usuario.h"


 Usuario::Usuario(std::string nombre_, std::string id_) : nombre(nombre_), id(id_) {
    for(int i =0;i<MAX_USUARIO;i++){
        materialesPrestados[i]=nullptr;
    }
    numerosMaterialesEnUso=0;
 }

std::string Usuario::getNombre() {
    return nombre;
}

void Usuario::setNombre(std::string nombre_) {
    nombre = nombre_;
}

std::string Usuario::getId() {
    return id;
}

void Usuario::setId(std::string id_) {
    id = id_;
}

MaterialBibliografico *Usuario::getMaterialPrestado(int index) {
    return materialesPrestados[index];
}

int Usuario::getNumerosMaterialesEnUso() {
    return numerosMaterialesEnUso;
}

void Usuario::setNumerosMaterialesEnUso(int numerosMaterialesEnUso_) {
    numerosMaterialesEnUso = numerosMaterialesEnUso_;
}

void Usuario::setMaterialPrestado(MaterialBibliografico *material, int index) {
    materialesPrestados[index] = material;
}
void Usuario::prestarMaterial(MaterialBibliografico *material) {
    materialesPrestados[getNumerosMaterialesEnUso()]=material;
   
    setNumerosMaterialesEnUso(getNumerosMaterialesEnUso()+1);
}
void Usuario::devolverMaterial(MaterialBibliografico *material) {
    bool found;
    int index;
    for(int i =0; i < MAX_USUARIO ; i++){
        if(found==false && materialesPrestados[i]->getTitulo()==material->getTitulo()){
            numerosMaterialesEnUso--;
            materialesPrestados[i]=nullptr;
            found=true;
            index=i;
 

        }
        if(found){
            if(i==MAX_USUARIO-1){ // last element
                materialesPrestados[i]=nullptr;
                break;

            }
            materialesPrestados[i]=materialesPrestados[i+1];
            materialesPrestados[i+1]=nullptr;
        }
    }
    
    // if(found){
    //     for (int i = index; i <5; i++)
    //     {
    //         if(i==4){ // last element
    //             materialesPrestados[i]=nullptr;
    //               break;

    //         }
    //         materialesPrestados[i]=materialesPrestados[i+1];
    //         materialesPrestados[i+1]=nullptr;
    //     }
        
    // }
}
std::string Usuario::getInfoPrestados(){
    std::string response="";
    for(int i =0 ; i < MAX_USUARIO ; i++){
        if(materialesPrestados[i]!=nullptr){

            response+= materialesPrestados[i]->getInformacion();
        }
    }
    return response;
}

 
Usuario::~Usuario(){
    for (int i = 0; i < MAX_USUARIO; i++) {
        if (materialesPrestados[i] != nullptr) {
            materialesPrestados[i]->setIsPrestado("disponible");
            materialesPrestados[i] = nullptr;
        }
    }

        
}
 