#ifndef MATERIAL_BIBLIOGRAFICO_H
#define MATERIAL_BIBLIOGRAFICO_H
 
#include "Libro.h"
#include "Revista.h"
// #include <bits/stdc++.h>
#include "Usuario.h"
class Sistema
{
private:
    MaterialBibliografico *biblioteca[100];
    int numerMateriales; // assumed 'tamanho' is the size of the biblioteca array
    Libro *libros[100];
    int numeroLibros;
    Revista *revistas[100];
    int numeroRevistas;
    Usuario *usuarios[100];
    int numeroUsuarios;

public:
    bool agregarMaterial(std::string);
    void mostrarInfoMateriales();
    void buscarMaterial();
    void prestarMaterial();
    void devolverMaterial();
    void guardarDatos();
    void leerDatos();
    ~Sistema();
};
#endif