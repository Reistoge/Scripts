archivo=open('ejercicio1.txt','r')
linea=archivo.readline().strip()
import numpy as np
import heapq as hq
partes=linea.split(',')
matriz=np.zeros([int(partes[0]),int(partes[1])])
for filas in range(int(partes[0])):
    linea=archivo.readline().strip()
    partes2=linea.split(',')
    for columnas in range(int(partes[1])):
        matriz[filas][columnas]=partes2[columnas]
print(matriz)
lista=[]
for filas2 in range(5):
    for columnas2 in range(3):
        lista.append(int(matriz[filas2][columnas2]))
mayor=hq.nlargest(3,lista)
print(mayor)