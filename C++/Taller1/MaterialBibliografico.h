#include <iostream>
class MaterialBibliografico{
    protected:
        std::string nombre,isbn,autor;
        bool estado;
        MaterialBibliografico(std::string _nombre, std::string _isbn,std::string _autor,bool _estado);
        virtual void mostrarInformacion();
        std::string getNombre();
        void setNombre(std::string value);
        std::string getIsbn();
        void setIsbn(std::string value);
        std::string getAutor();
        void setAutor(std::string value);
        bool getEstado();
        void setEstado(bool value);
    



    
};
 