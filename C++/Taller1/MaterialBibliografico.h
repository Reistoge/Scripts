#pragma once
#include <iostream>
class MaterialBibliografico
{
protected:
    std::string titulo, isbn, autor;
    std::string isPrestado;
    Usuario*  usuarioDelMaterial;
    MaterialBibliografico(std::string nombre_, std::string isbn_, std::string autor_, std::string estado_);

public:
    virtual void mostrarInformacion();
    virtual std::string getInformacion();
    std::string getTitulo();
    void setTitulo(std::string value);
    std::string getIsbn();
    void setIsbn(std::string value);
    std::string getAutor();
    void setAutor(std::string value);
    std::string getIsPrestado();
    void setIsPrestado(std::string value);
};
