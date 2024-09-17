#pragma once
#include "MaterialBibliografico.h"
#include "Libro.h"
#include "Revista.h"
// #include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <sstream>
#include "Usuario.h"
#include <fstream>

#define MAX_BIBLIOTECA 100
class Sistema
{
private:
    MaterialBibliografico *biblioteca[MAX_BIBLIOTECA];
    int numeroMateriales;
    Libro *libros[MAX_BIBLIOTECA];
    int numeroLibros;
    Revista *revistas[MAX_BIBLIOTECA];
    int numeroRevistas;
    Usuario *usuarios[MAX_BIBLIOTECA];
    int numeroUsuarios;

public:
    Sistema();
    bool agregarMaterial(std::string);
    void mostrarInfoMateriales();
    bool buscarMaterial(std::string input);
    MaterialBibliografico *getMaterial(std::string idMaterial);
    Usuario *getUsuario(std::string idUsuario);
    bool crearUsuario(std::string input);
    bool eliminarUsuario(std::string input);

    bool devolverMaterial(std::string idUsuario, std::string infoMaterial);
    bool prestarMaterial(std::string idMaterial, std::string idUsuario);
    std::string buscarUsuarioPorNombre(std::string input);
    std::string buscarUsuarioPorID(std::string input);
    std::vector<std::string> split(std::string word, char key);
    void readUsuarios(std::string filename);
    void writeMateriales(std::string filename);
    void readMateriales(std::string filename);
    void writeUsuarios(std::string filename);
    std::string buscarUsuarioHandler(std::string input);
    bool  existeMaterial(std::string tipo, std::string titulo);
    std::string toLowercase(std::string str);
    void guardarDatos();
    void leerDatos();
    ~Sistema();
};