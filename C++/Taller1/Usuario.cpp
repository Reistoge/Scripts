
#include "Usuario.h"

Usuario::Usuario(std::string id_, std::string nombre_) : nombre(nombre_), id(id_)
{
    for (int i = 0; i < MAX_USUARIO; i++)
    {
        materialesPrestados[i] = nullptr;
    }
    numerosMaterialesEnUso = 0;
}

std::string Usuario::getNombre()
{
    return nombre;
}

void Usuario::setNombre(std::string nombre_)
{
    nombre = nombre_;
}

std::string Usuario::getId()
{
    return id;
}

void Usuario::setId(std::string id_)
{
    id = id_;
}

MaterialBibliografico *Usuario::getMaterialPrestado(int index)
{
    return materialesPrestados[index];
}

int Usuario::getNumerosMaterialesEnUso()
{
    return numerosMaterialesEnUso;
}

void Usuario::setNumerosMaterialesEnUso(int numerosMaterialesEnUso_)
{
    numerosMaterialesEnUso = numerosMaterialesEnUso_;
}

void Usuario::setMaterialPrestado(MaterialBibliografico *material, int index)
{
    materialesPrestados[index] = material;
}
void Usuario::prestarMaterial(MaterialBibliografico *material)
{

    materialesPrestados[getNumerosMaterialesEnUso()] = material;
    setNumerosMaterialesEnUso(getNumerosMaterialesEnUso() + 1);
    material->setUsuarioDelMaterial(this);
}
void Usuario::devolverMateriales()
{
    // se reccore la lista de materiales y se actualiza al  usuario que lo tiene prestado
    for (int i = 0; i <= numerosMaterialesEnUso; i++)
    {
        if (materialesPrestados[i] != nullptr)
        {
            materialesPrestados[i]->setUsuarioDelMaterial(nullptr);
        }
    }
}
void Usuario::devolverMaterial(MaterialBibliografico *material)
{
    /*
      Se recorre toda la lista de materiales prestados
      hasta encontrar el material con igual titulo que
      el solicitado y aplica la logica para devolver el material
    */
    bool found = false;
    int index = 0;
    for (int i = 0; i < MAX_USUARIO; i++)
    {
        if (found == false && materialesPrestados[i]->getTitulo() == material->getTitulo())
        {
            materialesPrestados[i] = nullptr;
            numerosMaterialesEnUso--;
            found = true;
            index = i;
        }
        if (found)
        {
            material->setUsuarioDelMaterial(nullptr);
            if (i == MAX_USUARIO - 1)
            { // last element
                materialesPrestados[i] = nullptr;
                break;
            }
            materialesPrestados[i] = materialesPrestados[i + 1];
            materialesPrestados[i + 1] = nullptr;
        }
    }
}
std::string Usuario::getInfoPrestados()
{
    /*
    Esta funcion recorre toda la lista de materiales
    prestados y devuelve una cadena con la informacion de cada material
    */
    std::string response = std::to_string(getNumerosMaterialesEnUso()) + "\n\n";
    for (int i = 0; i < MAX_USUARIO; i++)
    {
        if (materialesPrestados[i] != nullptr)
        {

            response += std::to_string(i + 1) + "." + materialesPrestados[i]->getInformacion() + "\n\n";
        }
    }
    return response + "\n";
}
std::string Usuario::getInfo()
{
    return "\nNombre: " + nombre + "\nID: " + id + "\nMateriales prestados: " + getInfoPrestados();
}
std::string Usuario::toString()
{
    return id + ";" + nombre;
}

Usuario::~Usuario()
{
    /*
        Se  eliminan todos los materiales prestados
    */
    for (int i = 0; i < MAX_USUARIO; i++)
    {
        if (materialesPrestados[i] != nullptr)
        {

            materialesPrestados[i] = nullptr;
        }
    }
}
