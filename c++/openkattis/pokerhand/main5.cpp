// Una posible solución es usar un mapa para almacenar la frecuencia de cada letra
#include <iostream>
#include <map>
using namespace std;

int main() {
  // Pedir al usuario que ingrese una palabra
  cout << "Ingrese una palabra: ";
  string palabra;
  cin >> palabra;

  // Crear un mapa vacío para guardar las frecuencias
  map<char, int> frecuencias;

  // Recorrer cada letra de la palabra y actualizar el mapa
  for (char letra : palabra) {
    // Si la letra ya está en el mapa, incrementar su frecuencia en uno
    if (frecuencias.count(letra) > 0) {
      frecuencias[letra]++;
    }
    // Si la letra no está en el mapa, agregarla con frecuencia uno
    else {
      frecuencias[letra] = 1;
    }
  }

  // Mostrar el resultado
  cout << "La frecuencia de cada letra es:\n";
  for (auto par : frecuencias) {
    cout << par.first << ": " << par.second << "\n";
  }

  return 0;
}