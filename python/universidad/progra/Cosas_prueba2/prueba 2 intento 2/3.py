# Leer el archivo de movidas
with open('movidas.txt', 'r') as file:
    movidas = file.readlines()

# Inicializar el tablero
tablero = [0] * 7  # Asumiendo que el tablero tiene 7 columnas

# Función para actualizar el tablero después de cada movimiento
def actualizar_tablero(jugador, columna):
    tablero[columna] += 1
    # Verificar si se debe eliminar la columna
    if tablero[columna] == 4:  # Asumiendo que una columna se llena con 4 fichas
        tablero[columna] = 0
    # Verificar si hay diferencia de dos fichas entre jugadores
    for i in range(len(tablero)):
        if tablero[i] >= 2:  # Asumiendo que la diferencia debe ser de 2 fichas
            tablero[i] = 0

# Simular el juego
jugador_actual = 1  # Asumiendo que el jugador 1 comienza
for movida in movidas:
    columna = int(movida.strip()) - 1  # Convertir la movida a índice de columna
    actualizar_tablero(jugador_actual, columna)
    # Cambiar de jugador
    jugador_actual = 2 if jugador_actual == 1 else 1

# Determinar el ganador
if jugador_actual == 1:
    print("El ganador es el jugador 2")
else:
    print("El ganador es el jugador 1")
