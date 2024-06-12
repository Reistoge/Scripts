# ejercicio 1
import numpy as np
def buscar_agregar(lista,elemento):
    if not elemento in lista:
        lista.append(elemento)
    return lista.index(elemento)

arch=open("ciudades.txt",encoding="utf-8")
linea=arch.readline()
ciudades=[]

distancias=np.zeros([10,10])
while linea!="":
    partes=linea.split(",")
    origen=partes[0].upper()
    destino=partes[1].upper()
    dist=float(partes[2])
    
    f=buscar_agregar(ciudades, origen)
    c=buscar_agregar(ciudades, destino)
    distancias[f][c]=dist
    distancias[c][f]=dist
    print(f,c)
    linea=arch.readline().strip()
    
    
    
    
    
    
    
    
    
    

arch.close()
arch=open("preguntas.txt",encoding="utf-8")

linea=arch.readline().strip()


while linea!="":
    partes=linea.split(",")
    origen=partes[0].upper().strip()
    destino=partes[1].upper().strip()
    if not origen in ciudades:
        print(origen,"no existe")
        
    elif not destino in ciudades:
        print(destino,"no existe")
    else:
        f=ciudades.index(origen)
        c=ciudades.index(destino)
        if distancias[f][c]>0:
            print(origen,"y",destino,"estan a",distancias[f][c],)
    
        else:
            print(origen," y ", destino," no estan conectados")
        print(f,c)
    linea=arch.readline().strip()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        