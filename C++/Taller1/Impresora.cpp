#include "Impresora.h"

void Impresora::menu()
{
     
    std::cout << "==============================\n"
              << "  Biblioteca - Menu Principal\n"
              << "==============================\n"
              << "  1. Agregar Material a la Biblioteca\n"
              << "  2. Mostrar Informacion de los Materiales\n"
              << "  3. Buscar Material\n"
              << "  4. Prestar Material\n"
              << "  5. Devolver Material\n"
              << "  6. Gestion de Usuarios\n"
              << "  7. Salir\n"
              << "==============================\n"
              << "\nSeleccione una opcion: ";

}
void Impresora::imprimir(std::string l,bool saltar){
    std::cout << l ;
    if(saltar){
        std::cout << std::endl;
    }
}
void Impresora::showAgregarMaterial()
{
    std::cout << std::string(10, '\n');
    std::cout << "=============================================\n"
            << "  Agregar Material a la Biblioteca\n"
            << "=============================================\n"
            << "Por favor ingrese los siguientes datos:\n"
            << "  - Tipo de material (Libro/Revista)\n"
            << "  - Titulo del material\n"
            << "  - ISBN del material\n"
            << "  - Autor del material\n"
            << "  - Estado del material (disponible/idUser)\n"
            << "  - Parametros extras\n"
            << "Ejemplo: Libro;El principito;1-4028-9462-7;Antoine de Saint-Exupery;disponible;06/04/1943;original y divertido\n"
            << "---------------------------------------------------------\n"
            << "Ingrese los datos solicitados separados por punto coma (,)\n"
            << "\n--------------------------------\n";
}
void Impresora::showMostrarInformacion()
{
    std::cout << std::string(10, '\n');

    std::cout << "2. Mostrar Informacion de los Materiales\n"
              << "--------------------------------\n";
              
}
void Impresora::showBuscarMaterial()
{
std::cout << std::string(10, '\n');
std::cout << "=============================================\n"
          << "  Buscar Material\n"
          << "=============================================\n"
          << "Por favor ingrese los siguientes datos:\n"
          << "  - Criterio de busqueda (Titulo/Autor)\n"
          << "  - Termino de busqueda\n"
          << "Ejemplo: Titulo;El principito\n"
          << "---------------------------------------------------------\n"
          << "Ingrese los datos solicitados separados por punto coma (;)\n"
          << "\n--------------------------------\n";
}
void Impresora::showPrestarMaterial()
{
    std::cout << std::string(10, '\n');
    std::cout << "=============================================\n"
            << "  Prestar Material\n"
            << "=============================================\n"
            << "Por favor ingrese los siguientes datos:\n"
            << "  - ID del usuario\n"
            << "  - Titulo del material\n"
            << "Ejemplo: 1234;El principito\n"
            << "---------------------------------------------------------\n"
            << "Ingrese los datos solicitados separados por punto coma (;)\n"
            << "\n--------------------------------\n";
}
void Impresora::showDevolverMaterial()
{
    std::cout << std::string(10, '\n');
    std::cout << "=============================================\n"
            << "  Devolver Material\n"
            << "=============================================\n"
            << "Por favor ingrese los siguientes datos:\n"
            << "  - ID del usuario\n"
            << "  - Titulo del material\n"
            << "Ejemplo: 12345;El principito\n"
            << "---------------------------------------------------------\n"
            << "Ingrese los datos solicitados separados por punto coma (;)\n"
            << "\n--------------------------------\n";
}
void Impresora::showGestionUsuarios()
{
    std::cout << std::string(10, '\n');
    std::cout << "6. Gestion de Usuarios\n"
              << "--------------------------------\n"
              << "  1. Crear Usuario\n"
              << "  2. Buscar Usuario\n"
              << "  3. Eliminar Usuario\n"
              << "  4. Volver al Menu Principal\n"
              << "\nSeleccione una opcion: \n"
              << "\n--------------------------------\n";
}
void Impresora::showCrearUsuario()
{
    std::cout << "=============================================\n"
            << "  Crear Usuario\n"
            << "=============================================\n"
            << "Por favor ingrese los siguientes datos:\n"
            << "  - ID del usuario\n"
            << "  - Nombre del usuario\n"
            << "Ejemplo: 1234;Juan\n"
            << "---------------------------------------------------------\n"
            << "Ingrese los datos solicitados separados por punto coma (;)\n"
            << "\n--------------------------------\n";
}
void Impresora::showBuscarUsuario()
{
    std::cout << std::string(10, '\n');
    std::cout << "=============================================\n"
            << "  Buscar Usuario\n"
            << "=============================================\n"
            << "Por favor ingrese los siguientes datos:\n"
            << "  - Criterio de busqueda (ID/Nombre)\n"
            << "  - Termino de busqueda\n"
            << "Ejemplo: ID;1234\n"
            << "---------------------------------------------------------\n"
            << "Ingrese los datos solicitados separados por punto coma (,)\n"
            << "\n--------------------------------\n";
}
void Impresora::showEliminarUsuario()
{
    std::cout << "=============================================\n"
            << "  Eliminar Usuario\n"
            << "=============================================\n"
            << "Por favor ingrese los siguientes datos:\n"
            << "  - ID del usuario\n"
            << "Ejemplo: 1234\n"
            << "---------------------------------------------------------\n"
            << "Ingrese el ID del usuario: \n"
            << "\n--------------------------------\n";
}
void Impresora::showVolverMenu()
{
    std::cout << std::string(10, '\n');
    std::cout << "4. Volver al Menu Principal\n"
              << "--------------------------------\n";
};