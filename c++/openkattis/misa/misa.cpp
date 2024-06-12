#include <iostream>
#include <string>
 
   

using namespace std;
bool valid(int x,int y,int A, int B){
    
    return(x>=0 && x<A && y>=0 && y<B);
}
int main() {
    int R,S;
    cin >> R;
    cin >> S;
    
    int** matrix = new int*[R]; // crear un arreglo de punteros a enteros
    // iterar las filas
    for (int i = 0; i < R; i++) {
        matrix[i] = new int[S]; // crear un arreglo de enteros para cada fila
    }
    for(int i=0; i<R;i++){

        for(int j=0;j<S;j++){
            char value;
            cin >> value;
            if(value=='.'){
                matrix[i][j] = 0;
            }
            else if(value=='o'){
                matrix[i][j]=1;
            }
            
        }
    }
    // bucle que imprime la matriz
    /* for(int i=0; i<R;i++){
        for(int j=0;j<S;j++){
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    } */

    int max=0;
    int pos_max[2];
    int contador;
    // Itermos la matriz
    // Primero iteramos las filas
    for(int i=0; i<R;i++){
        // Despues las columnas        
        for(int j=0;j<S;j++){
            // Verifico si me puedo sentar en la posicion actual
            if(matrix[i][j]==0){
                //se sienta
                // Creo un contador para esta posición (i, j)
                contador=0;
                // Creo 2 bucles para analizar la cantidad
                // de personas que tengo al rededor de mi posicion
                // actual (que es [i, j])
                // ITero las filas
                for(int k=i-1;k<=i+1;k++){ // Apartir de aqui los bulces me dejaran listo el contador
                    // Itero las columnas
                    for(int z=j-1; z<=j+1;z++){
                        // Si es que la posicion que "podria" saludar
                        // es valida y además contiene a una persona
                        // aumento el contador.
                        // Si la posicion no es valida porque escapa
                        // de los margenes de la matriz. no hago nada
                        if (valid(k,z,R,S)&&!(k==i && z==j)){
                            //verifico si es que existe una persona en
                            // la casilla ya valida
                            if(matrix[k][z]==1){
                                // si hay una persona aumento el contador
                                contador+=1;
                            }
                        }
                    }
                }
                // A partir de aqui, mi contador estará listo con
                // la cantidad de personas a las que puedo saludar

                if (contador > max){
                    // actualizo el valor maximo por el actual
                    max = contador;
                    // Guardo la posicion actual
                    pos_max[0] = i;
                    pos_max[1] = j;
                    // Esta es la posicion donde se sentara mirko
                }
                
            }
            
        }
        
    }
    // Sentamos al mirko y lo convertimos en una persona más para volver a reiniciar el bucle.
    if(max!=0){
        matrix[pos_max[0]][pos_max[1]] = 1;
    }
    // reiniciamos el contador para volver a contar el numero de personas que se saludan
    
    contador=0;
    // Itermos la matriz pero esta vez las iteramos sacando cada saludo entre las personas para calcular los saludos totales.

    // Primero iteramos las filas
    for(int i=0; i<R;i++){
        // Despues las columnas        
        for(int j=0;j<S;j++){
            // Verifico si me puedo sentar en la posicion actual
            if(matrix[i][j]==1){
                //se sienta
                // Creo un contador para esta posición (i, j)
                
                // Creo 2 bucles para analizar la cantidad
                // de personas que tengo al rededor de mi posicion
                // actual (que es [i, j])
                // ITero las filas
                for(int k=i-1;k<=i+1;k++){ // Apartir de aqui los bulces me dejaran listo el contador
                    // Itero las columnas
                    for(int z=j-1; z<=j+1;z++){
                        // Si es que la posicion que "podria" saludar
                        // es valida y además contiene a una persona
                        // aumento el contador.
                        // Si la posicion no es valida porque escapa
                        // de los margenes de la matriz. no hago nada
                        if (valid(k,z,R,S)&&!(k==i && z==j)){
                            //verifico si es que existe una persona en
                            // la casilla ya valida
                            if(matrix[k][z]==1){
                                // si hay una persona aumento el contador
                                contador+=1;
                            }
                        }
                    }
                }
                
            }
            
        }
        
    }
    contador/=2;
    cout << contador;
    

    
    

}