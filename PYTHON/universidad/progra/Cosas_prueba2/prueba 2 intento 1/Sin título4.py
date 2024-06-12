

import numpy as np
def mayor_columna(mtx):
    mayor=0
    suma=0
    mas_jugados=[]
    for cols in range(mtx.shape[1]):
        suma=0
        for fila in range(mtx.shape[0]):
            suma+=mtx[fila][cols]
        if suma>mayor:
            mayor=suma
            mas_jugados.clear()
            mas_jugados.append(lista_juegos[cols])
        elif suma==mayor:
            mas_jugados.append(lista_juegos[cols])
    return mas_jugados
def menor_columna(mtx):
    menor=10**10
    jugador_record=""
    for cols in range(mtx.shape[1]):
        menor=10**10
        for fila in range(mtx.shape[0]):
            if mtx[fila][cols]!=0:
                if mtx[fila][cols]<menor:
                    menor=mtx[fila][cols]
                    jugador_record=lista_amigos[fila]
        if menor!=10**10:  
            print(f"{lista_juegos[cols]} fue terminado en {menor} por {jugador_record}")
def bonus():
    suma1=0
    for i in range(mtx_veces.shape[0]):
        
        for j in range(mtx_veces.shape[1]):
            suma1+=mtx_veces[i][j]
        if i >=len(lista_amigos):
            break
    for i in range(mtx_veces.shape[0]):
        suma2=0
        for j in range(mtx_veces.shape[1]):
            suma2+=mtx_veces[i][j]
        if i >=len(lista_amigos):
            break
        print(f"{lista_amigos[i]} {suma2/suma1}")
    
    print(suma1)
            
            
                
         
     
def mayor_elemento(mtx):
    mayor=0
    viciados=[]
    nombre_juego=[]
    for i in range(mtx.shape[0]):
        for j in range(mtx.shape[1]):
            if mtx[i][j]>mayor:
                mayor=mtx[i][j]
                viciados.clear()
                nombre_juego.clear()
                viciados.append(lista_amigos[i])
                nombre_juego.append(lista_juegos[j])
            elif mtx[i][j]==mayor:
                viciados.append(lista_amigos[i])
                nombre_juego.append(lista_juegos[j])
    return [mayor,viciados,nombre_juego]
                
def jugador(mtx_horas):
    promedios=[]
    for i in range(len(lista_amigos)):
        suma=0
        juegos=0
        print(lista_amigos[i])
        for j in range(mtx_horas.shape[1]):
            if mtx_horas[i][j]!=0:
                suma+=mtx_horas[i][j]
                juegos+=1
                print(lista_juegos[j],mtx_horas[i][j])
        prom=suma/juegos
        promedios.append(prom)
    print()
    for i in range(len(lista_amigos)):
        print(lista_amigos[i], promedios[i])
        
        

arch=open("juegos_amistad.txt")
linea=arch.readline().strip()
mtx_horas=np.zeros([10,50])
mtx_veces=np.zeros([10,50])
lista_amigos=[]
lista_juegos=[]

while linea!="":
    partes=linea.split(",")
    amigo=partes[0]
    juego=partes[1]
    tiempo=int(partes[2])
    if amigo not in lista_amigos:
        lista_amigos.append(amigo)
    if juego not in lista_juegos:
        lista_juegos.append(juego)
    if mtx_horas[lista_amigos.index(amigo)][lista_juegos.index(juego)]==0:
        mtx_horas[lista_amigos.index(amigo)][lista_juegos.index(juego)]=tiempo
    elif tiempo<mtx_horas[lista_amigos.index(amigo)][lista_juegos.index(juego)]: 
        mtx_horas[lista_amigos.index(amigo)][lista_juegos.index(juego)]=tiempo
    
    mtx_veces[lista_amigos.index(amigo)][lista_juegos.index(juego)]+=1
        
    
    linea=arch.readline().strip()
    


print("--------------------------------------------------------------------------------")
print("Pregunta 1")
print("El o los juegos más jugados fueron:") 
print(f" {mayor_columna(mtx_veces)}" )
print("--------------------------------------------------------------------------------")

print("--------------------------------------------------------------------------------")
print("Pregunta 2")
print(f" {mayor_elemento(mtx_veces)}" )
print("--------------------------------------------------------------------------------")
jugador(mtx_horas)
menor_columna(mtx_horas)
bonus()

