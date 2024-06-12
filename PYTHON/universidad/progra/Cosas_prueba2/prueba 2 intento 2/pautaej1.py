#
import numpy as np

# 5 1 4 6 5 3 7 9 5 6 4 3 4 5 1 2 3 1 3 2 5 3
# 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1



def eliminarColumna(tablero, columna, numColumnas):
	#print("Eliminando columna", columna)
	for c in range(columna, numColumnas - 1):
		for f in range(0, tablero.shape[0]):
			tablero[f][c] = tablero[f][c+1]
	numColumnas -= 1
	return numColumnas

def printTablero(tablero, numColumnas):
	for f in range(0, tablero.shape[0]):
		linea = ""
		for c in range(0, numColumnas):
			linea += str(int(tablero[f][c])) + " "
		print(linea)
	print("-------------------")

def jugar(tablero, numColumnas, jugador, columna):
	columna -= 1
	#print("jugando jugador", jugador, "col", columna)
	if columna < 0 or columna >= numColumnas:
		print("\tMovida inválida jugador", jugador, "índice", columna)
		return numColumnas

	objetivo = -1
	for f in range(tablero.shape[0] - 1, -1, -1):
		if tablero[f][columna] == 0:
			objetivo = f
			break
	if objetivo == -1:
		print("\tMovida inválida jugador", jugador, "índice", columna)
		return numColumnas

	tablero[objetivo][columna] = jugador

	if objetivo == 0:
		#print("objetivo", 0)
		#printTablero(tablero, numColumnas)
		numColumnas = eliminarColumna(tablero, columna, numColumnas)
	else:
		cont1 = 0
		cont2 = 0
		for f in range(0, tablero.shape[0]):
			if tablero[f][columna] == 1:
				cont1 += 1
			if tablero[f][columna] == 2:
				cont2 += 1
		if cont1 - cont2 >= 2 or cont2 - cont1 >= 2:
			#print("sobre pos")
			#printTablero(tablero, numColumnas)
			numColumnas = eliminarColumna(tablero, columna, numColumnas)

	return numColumnas

arch = open("movidas1.txt", "r")

linea = arch.readline().strip()
sim = 0
while linea != "":
	sim += 1
	partes = linea.split(" ")
	numColumnas = int(partes[0])
	tablero = np.zeros([numColumnas,numColumnas])
	jugador = int(partes[1])
	#printTablero(tablero, numColumnas)
	print("Simulación", sim, "inicia jugador", jugador, "con tablero tamaño", numColumnas)

	for i in range(2, len(partes)):
		numColumnas = jugar(tablero, numColumnas, jugador, int(partes[i]))
		if numColumnas == 0:
			print("\tgana jugador", jugador)
			break
		#printTablero(tablero, numColumnas)
		jugador += 1
		if jugador > 2: jugador = 1

	if numColumnas != 0:
		print("\tsin ganador")

	linea = arch.readline().strip()