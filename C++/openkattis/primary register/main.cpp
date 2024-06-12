#include <iostream>
#include <vector>
// https://open.kattis.com/problems/register


// tenemos que saber basicamente cuando se llena las entradas principales

using namespace std;

int main() {
    vector<int> current_state(8); // Estado actual de los registros
    vector<int> final_state = {1, 2, 4, 6, 10, 12, 16, 18}; // Estado final antes del desbordamiento

    // Leer el estado actual de los registros desde la entrada estándar
    for (int & value : current_state) {
        cin >> value;
    }

    int steps = 0; // Contador de pasos

    // Si el último registro (registro 7, para el número primo 19) aún no ha alcanzado su valor máximo,
    // incrementamos este registro hasta que alcance 18 y sumamos los pasos correspondientes.
    while (current_state[7] < 18) {
        steps += 510510; // 510510 es el producto de los primeros 7 números primos (2*3*5*7*11*13*17)
        current_state[7]++;
    }
    
    // Procesar el incremento de los registros desde el estado actual hasta el estado final
    while (current_state != final_state) {
        // Incrementamos el primer registro y sumamos un paso
        current_state[0]++;
        steps++;

        // Verificamos y manejamos el desbordamiento para cada registro,
        // pasando al siguiente registro si es necesario.
        if (current_state[0] == 2) {
            current_state[0] = 0;
            current_state[1]++;
        }
        if (current_state[1] == 3) {
            current_state[1] = 0;
            current_state[2]++;
        }
        if (current_state[2] == 5) {
            current_state[2] = 0;
            current_state[3]++;
        }
        if (current_state[3] == 7) {
            current_state[3] = 0;
            current_state[4]++;
        }
        if (current_state[4] == 11) {
            current_state[4] = 0;
            current_state[5]++;
        }
        if (current_state[5] == 13) {
            current_state[5] = 0;
            current_state[6]++;
        }
        if (current_state[6] == 17) {
            current_state[6] = 0;
            current_state[7]++;
        }
    }

    // Imprimir el total de pasos necesarios
    cout << steps << endl;

    return 0;
}