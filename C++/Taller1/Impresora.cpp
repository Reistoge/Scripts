
#include "Impresora.h"

void Impresora::menu()
{
     
    std::cout << "==============================\n"
              << "  Biblioteca - Menu Principal\n"
              << "==============================\n"
              << "1. Agregar Material a la Biblioteca\n"
              << "2. Mostrar Informacion de los Materiales\n"
              << "3. Buscar Material\n"
              << "4. Prestar Material\n"
              << "5. Devolver Material\n"
              << "6. Gestion de Usuarios\n"
              << "7. Salir\n"
              << "==============================\n"
              << "\nSeleccione una opcion: \n";

}
void Impresora::imprimir(std::string l,bool saltar){
    std::cout << l ;
    if(saltar){
        std::cout << std::endl;
    }
}
void Impresora::showAgregarMaterial()
{
    std::cout << std::string(100, '\n');
    std::cout << "1. Agregar Material a la Biblioteca\n"
              << "--------------------------------\n"
              << "Formato(Libro/Revista), nombre, isbn, autor, prestado (idUser/disponible) , parametros Extras : \n"
              << "Por favor ingrese los datos solicitados separados por coma (,)\n"
               
              << "Ej1: Libro, El principito, 1-4028-9462-7, Antoine de Saint-Exupery, disponible, 06/04/1943, original y divertido \n"
              << "Ej2: Revista, Club Nintendo, 978-1-4028-9462-6, Nintendo MX, 98234, 13, Agosto\n"
              << "[Validar que no se exceda el tamanho maximo del array]\n"
              << "\n--------------------------------\n";
    
}
void Impresora::showMostrarInformacion()
{
    std::cout << std::string(100, '\n');

    std::cout << "2. Mostrar Informacion de los Materiales\n"
              << "--------------------------------\n";
              
}
void Impresora::showBuscarMaterial()
{
    std::cout << std::string(100, '\n');
    std::cout << "3. Buscar Material\n"
              << "--------------------------------\n"
              << "Criterio de busqueda (Título/Autor), termino de busqueda: \n"
              << "Por favor ingrese los datos solicitados separados por coma (,)\n"
              << " \n"
              << "[Resultados de la busqueda]\n"
              << "\n--------------------------------\n";
}
void Impresora::showPrestarMaterial()
{
    std::cout << std::string(100, '\n');
    std::cout << "4. Prestar Material\n"
              << "--------------------------------\n"
              << "Ingrese el titulo del material a prestar: \n"
              << "Ingrese el ID del usuario: \n"
              << "[Actualizar el estado prestado del material y registrarlo en el array materialesPrestados del Usuario]\n"
              << "\n--------------------------------\n";
}
void Impresora::showDevolverMaterial()
{
    std::cout << std::string(100, '\n');
    std::cout << "5. Devolver Material\n"
              << "--------------------------------\n"
              << "Ingrese el titulo del material a devolver: \n"
              << "Ingrese el ID del usuario: \n"
              << "[Actualizar el estado del material]\n"
              << "\n--------------------------------\n";
}
void Impresora::showGestionUsuarios()
{
    std::cout << std::string(100, '\n');
    std::cout << "6. Gestión de Usuarios\n"
              << "--------------------------------\n"
              << "1. Crear Usuario\n"
              << "2. Buscar Usuario\n"
              << "3. Eliminar Usuario\n"
              << "4. Volver al Menú Principal\n"
              << "\nSeleccione una opción: \n"
              << "\n--------------------------------\n";
}
void Impresora::showCrearUsuario()
{
    std::cout << std::string(100, '\n');
    std::cout << "1. Crear Usuario\n"
              << "--------------------------------\n"
              << "Ingrese el nombre del usuario: \n"
              << "Ingrese el ID del usuario: \n"
              << "[Asociar materiales prestados a usuarios específicos]\n"
              << "\n--------------------------------\n";
}
void Impresora::showBuscarUsuario()
{
    std::cout << std::string(100, '\n');
    std::cout << "2. Buscar Usuario\n"
              << "--------------------------------\n"
              << "Ingrese el ID del usuario: \n"
              << "[Mostrar información del usuario y materiales prestados]\n"
              << "\n--------------------------------\n";
}
void Impresora::showEliminarUsuario()
{
    std::cout << std::string(100, '\n');
    std::cout << "3. Eliminar Usuario\n"
              << "--------------------------------\n"
              << "Ingrese el ID del usuario: \n"
              << "[Eliminar usuario y actualizar registros]\n"
              << "\n--------------------------------\n";
}
void Impresora::showVolverMenu()
{
    std::cout << std::string(100, '\n');
    std::cout << "4. Volver al Menú Principal\n"
              << "--------------------------------\n";
}