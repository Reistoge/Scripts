import numpy as np


def buscar_agregar(lista,elemento):
    if not elemento in lista:
        lista.append(elemento)
    return lista.index(elemento)
arch=open("visitas.txt",encoding="utf-8")
linea=arch.readline().strip()


paises=[]
nombres=[]
visitas=np.zeros([20,20])

while linea!="":
    partes=linea.split(",")
    nombre=partes[0]
    pais=partes[1]
    linea=arch.readline().strip()
    
    if not nombre in nombres:
        nombres.append(nombre)
    if not pais in paises:
        paises.append(pais)
    fila=buscar_agregar(nombres, nombre)
    columna=buscar_agregar(paises, pais)
    visitas[fila][columna]+=1
    print(fila,columna)
    linea=arch.readline()
    
for c in range(len(paises)):
    suma=0
    for f in range(len(nombres)):
        suma+=visitas[f][c]


lista_suma=[]
for c in range(len(paises)):
    suma=0
    for f in range(len(nombres)):
        suma+=visitas[f][c]
    lista_suma.append(suma)
    
maximo=max(lista_suma)
indice_max=lista_suma.index(maximo)
print("el pais más visitado es "+ paises[indice_max])
for f in range(len(nombres)):
    if visitas[f][indice_max]>0:
        print("-", nombres[f])
        
