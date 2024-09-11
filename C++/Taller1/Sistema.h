#pragma once
#include "MaterialBibliografico.h"
#include "Libro.h"
#include "Revista.h"
// #include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <sstream>
#include "Usuario.h"
#define MAX_BIBLIOTECA 100
class Sistema{
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
        MaterialBibliografico* getMaterial(std::string idMaterial);
        Usuario* Sistema::getUsuario(std::string idUsuario);
        bool crearUsuario(std::string input);
        bool eliminarUsuario(std::string input);
        bool prestarMaterial(std::string idUsuario, std::string infoMaterial);
        bool devolverMaterial(std::string idUsuario, std::string infoMaterial);
        std::string buscarUsuario(std::string input);
        void guardarDatos();
        void leerDatos();
        ~Sistema();
};