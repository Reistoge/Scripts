import numpy as np

def buscarAgregar(lista, elemento):
    if elemento not in lista:
        lista.append(elemento)
    return lista.index(elemento)

paises=[]
nombres=[]
anos=[]
mtx=np.zeros([10,10])


arch=open("visitas.txt")
linea=arch.readline().strip()

while linea!="":
    partes=linea.split(",")
    nombre=partes[0]
    pais=partes[1]
    ano=int(partes[2])
    paises.append(pais)
    nombres.append(nombre)
    anos.append(ano)
    
    
    linea=arch.readline().strip()
    
    
print(paises)
print(nombres)
print(anos)
print(mtx)