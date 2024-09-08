#include "Sistema.h"
#include <sstream>
#include <vector>
#include <algorithm>

Sistema::Sistema()
{
    for (int i = 0; i < 100; i++)
    {
        biblioteca[i] = nullptr;
        usuarios[i] = nullptr;
        this->numerMateriales=0;
        this->numeroLibros=0;
        this->numeroRevistas=0;
        this->numeroUsuarios=0;

        
    }
}
bool Sistema::agregarMaterial(std::string input)
{

    std::istringstream iss(input);
    std::string token;
    std::vector<std::string> attributes;
    // Split the input string into substrings separated by commas
    while (std::getline(iss, token, ','))
    {
        token.erase(0, token.find_first_not_of(" \t")); // remove leading whitespace
        token.erase(token.find_last_not_of(" \t") + 1); // remove trailing whitespace
        attributes.push_back(token);
    }
    // converting the string to lowercase
    std::string type = attributes[0];
    std::transform(type.begin(), type.end(), type.begin(),
                   [](unsigned char c)
                   { return std::tolower(c); });
    if (attributes.size() <= 6 && (attributes[4]=="prestado" || attributes[4]=="no prestado") && this->numerMateriales<=100)
    {
        return false;
    }
     
    if (type == "libro")
    {
       MaterialBibliografico* libro = new Libro(attributes[1],attributes[2],attributes[3],attributes[4]=="prestado",attributes[5],attributes[6]);
        this->numeroLibros++;
        this->numerMateriales++;
        this->biblioteca[this->numerMateriales - 1] = libro;
        this->libros[this->numeroLibros-1] = dynamic_cast<Libro*>(libro);
        return true;

    }
    else if (type == "revista")
    {
        
        MaterialBibliografico* revista = new Revista(attributes[1],attributes[2],attributes[3],attributes[4]=="prestado",std::stoi(attributes[5]),attributes[6]);
        this->numeroRevistas++;
        this->numerMateriales++;
        this->biblioteca[this->numerMateriales - 1] = revista;
        this->revistas[this->numeroRevistas-1] = dynamic_cast<Revista*>(revista);
        return true;
    }
    else{
        return false;
    }

};
void Sistema::mostrarInfoMateriales() {};
void Sistema::buscarMaterial() {};
void Sistema::prestarMaterial() {};
void Sistema::devolverMaterial() {};
Sistema::~Sistema()
{
    // Delete each element in the biblioteca array
    for (int i = 0; i < 100; i++)
    {
        if (biblioteca[i] != nullptr)
        {
            delete biblioteca[i];
        }
    }
    delete[] biblioteca;

    // Delete the biblioteca array

    // Delete each element in the usuarios array
    for (int i = 0; i < 100; i++)
    {
        if (usuarios[i] != nullptr)
        {
            delete usuarios[i];
        }
    }
    // Delete the usuarios array
    delete[] usuarios;
}
