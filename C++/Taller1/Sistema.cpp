#include "Sistema.h"
#include <sstream>
#include <vector>
Sistema::Sistema() {
    for (int i = 0; i < 100; i++) {
        biblioteca[i] = nullptr;
        usuarios[i] = nullptr;
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
    if(attributes.size()==6){
        
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
