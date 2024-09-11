
#include "Sistema.h"

Sistema::Sistema()
{
    for (int i = 0; i < MAX_BIBLIOTECA; i++)
    {
        biblioteca[i] = nullptr;
        usuarios[i] = nullptr;
        this->numeroMateriales = 0;
        this->numeroLibros = 0;
        this->numeroRevistas = 0;
        this->numeroUsuarios = 0;
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
    if (attributes.size() <= 6 && this->numeroMateriales <= MAX_BIBLIOTECA)
    {
        return false;
    }

    if (type == "libro")
    {
        try
        {
            MaterialBibliografico *libro = new Libro(attributes[1], attributes[2], attributes[3], attributes[4], attributes[5], attributes[6]);
            if (attributes[4] != "disponible")
            {
                Usuario *u = getUsuario(attributes[4]);
                if (u != nullptr)
                {
                    u->prestarMaterial(libro);
                }
                else
                {
                    return false;
                }
            }
            this->numeroLibros++;
            this->numeroMateriales++;
            this->biblioteca[this->numeroMateriales - 1] = libro;
            this->libros[this->numeroLibros - 1] = dynamic_cast<Libro *>(libro);
            return true;
        }
        catch (const std::exception &e)
        {

            return false;
        }
    }
    else if (type == "revista")
    {
        try
        {
            MaterialBibliografico *revista = new Revista(attributes[1], attributes[2], attributes[3], attributes[4], std::stoi(attributes[5]), attributes[6]);
            if (attributes[4] != "disponible")
            {
                Usuario *u = getUsuario(attributes[4]);
                if (u != nullptr)
                {
                    u->prestarMaterial(revista);
                }
                else
                {
                    return false;
                }
            }
            this->numeroRevistas++;
            this->numeroMateriales++;
            this->biblioteca[this->numeroMateriales - 1] = revista;
            this->revistas[this->numeroRevistas - 1] = dynamic_cast<Revista *>(revista);
            return true;
        }
        catch (const std::exception &e)
        {
            return false;
        }
    }
    else
    {
        return false;
    }
};
void Sistema::mostrarInfoMateriales()
{
    std::cout << "REVISTAS: \n\n";
    for (int i = 0; i < this->numeroRevistas; ++i)
    {
        this->revistas[i]->mostrarInformacion();
        std::cout << "\n";
    }

    std::cout << "\LIBROS:  \n\n";
    for (int i = 0; i < this->numeroLibros; ++i)
    {
        this->libros[i]->mostrarInformacion();
        std::cout << "\n";
    }
};
bool Sistema::buscarMaterial(std::string input)
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
    if (attributes.size() != 2)
        return false;
    std::string campo = attributes[0];
    std::string valor = attributes[1];
    if (campo == "autor")
    {
        for (int i = 0; i < this->numeroMateriales; ++i)
        {
            if (biblioteca[i]->getAutor() == valor)
            {
                if (dynamic_cast<Libro *>(biblioteca[i]))
                {
                    dynamic_cast<Libro *>(biblioteca[i])->mostrarInformacion();
                }
                else if (dynamic_cast<Revista *>(biblioteca[i]))
                {
                    dynamic_cast<Revista *>(biblioteca[i])->mostrarInformacion();
                }
            }
        }
    }
    else if (campo == "titulo")
    {
        for (int i = 0; i < this->numeroMateriales; ++i)
        {
            if (biblioteca[i]->getTitulo() == valor)
            {
                if (dynamic_cast<Libro *>(biblioteca[i]))
                {
                    dynamic_cast<Libro *>(biblioteca[i])->mostrarInformacion();
                }
                else if (dynamic_cast<Revista *>(biblioteca[i]))
                {
                    dynamic_cast<Revista *>(biblioteca[i])->mostrarInformacion();
                }
            }
        }
    }
}
MaterialBibliografico *Sistema::getMaterial(std::string idMaterial)
{
    for (int i = 0; i < numeroMateriales; i++)
    {
        if (biblioteca[i]->getTitulo() == idMaterial && biblioteca[i]->getIsPrestado() == "disponible")
        {

            return biblioteca[i];
        }
    }
    return nullptr;
}
Usuario *Sistema::getUsuario(std::string idUsuario)
{
    for (int i = 0; i < numeroUsuarios; i++)
    {
        if (usuarios[i]->getId() == idUsuario)
        {
            return usuarios[i];
        }
    }
    return nullptr;
}
bool Sistema::prestarMaterial(std::string idUsuario, std::string infoMaterial)
{
    MaterialBibliografico *material = getMaterial(infoMaterial);
    Usuario *usuario = getUsuario(idUsuario);
    if (material != nullptr && usuario != nullptr && usuario->getNumerosMaterialesEnUso() < 5)
    {
        usuario->prestarMaterial(material);
        material->setIsPrestado("disponible");
        return true;
    }
    else
    {
        return false;
    }
};
bool Sistema::devolverMaterial(std::string idUsuario, std::string infoMaterial)
{
    MaterialBibliografico *material = getMaterial(infoMaterial);
    Usuario *usuario = getUsuario(idUsuario);
    if (material != nullptr && usuario != nullptr && usuario->getNumerosMaterialesEnUso() < 5)
    {
        usuario->devolverMaterial(material);
        material->setIsPrestado("disponible");
        return true;
    }
    else
    {
        return false;
    }
};
bool Sistema::crearUsuario(std::string input)
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
    if (attributes.size() == 2 && numeroUsuarios < MAX_BIBLIOTECA)
    {
        Usuario *usuario = new Usuario(attributes[0], attributes[1]);

        usuarios[numeroUsuarios] = usuario;
        numeroUsuarios++;
        return true;
    }
    else
    {
        return false;
    }
}
bool Sistema::eliminarUsuario(std::string input)
{
    bool found = false;
    int index;
    Usuario *usuario = getUsuario(input);
    if (usuario != nullptr)
    {
        for (int i = 0; i < MAX_BIBLIOTECA; i++)
        {
            if (found==false && usuarios[i]->getId() == usuario->getId())
            {
                numeroUsuarios--;
                usuarios[i] = nullptr;
                found = true;
                index = i;
                continue;
            }
            if (found)
            {
                if (i == MAX_BIBLIOTECA-1)
                { // last element
                    usuarios[i] = nullptr;
                    break;
                }
                usuarios[i] = usuarios[i + 1];
                usuarios[i + 1] = nullptr;
            }
        }
        return true;
    }
    return false;
     
    
}
std::string Sistema::buscarUsuario(std::string  input){
    std::string response="";
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
    if(attributes.size()==2){
        Usuario* usuario = getUsuario(input);
        if(usuario!=nullptr){
            response+= "\n"+usuario->getId() + "\n"+usuario->getNombre() + usuario->getInfoPrestados();
        }

    }
    else if(attributes.size()==1){
        for (int i = 0; i < numeroUsuarios; i++){
            if(usuarios[i]->getNombre()==attributes[0] ||  usuarios[i]->getId()==attributes[1]){
                response+= "\n"+usuarios[i]->getId() + "\n"+usuarios[i]->getNombre() + usuarios[i]->getInfoPrestados();
            }
        }
        
    }
     
    
    return response;
}

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
