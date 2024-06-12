import numpy as np
def identificar_caminos(lista):
    camino=[]
    suma=0
    llegar=True
    for i in range(len(lista)):
        suma+=lista[i]
        if int(lista[i])==0:
            camino.append("hierba")
        elif int(lista[i])==1:
            camino.append("agua")
        elif int(lista[i])==2:
            camino.append("rocas")
        elif int(lista[i])==3:
            camino.append("fuego")
            llegar=False
            
    return [camino,llegar,suma]

            

    
            
def contar_arriba(mtx,posicion):
    numeros=[]
    fila_7=posicion[0]
    cols_7=posicion[1]
    
    for i in range(mtx.shape[0]-fila_7):
        if i<0:
            break
        if i >mtx.shape[0]:
            break
        numeros.append(mtx[i][cols_7])
    return numeros

def contar_abajo(mtx,posicion):
    numeros=[]
    fila_7=posicion[0]
    cols_7=posicion[1]
    
    for i in range(fila_7+1,mtx.shape[0],1):
        if i<0:
            break
        if i >mtx.shape[0]:
            break
        numeros.append(mtx[i][cols_7])
    return numeros
def contar_derecha(mtx,posicion):
    numeros=[]
    fila_7=posicion[0]
    cols_7=posicion[1]
    
    for i in range(cols_7+1,mtx.shape[1],1):
        if i<0:
            break
        if i >mtx.shape[1]:
            break
        numeros.append(mtx[fila_7][i])
    return numeros
def contar_izquierda(mtx,posicion):
    numeros=[]
    fila_7=posicion[0]
    cols_7=posicion[1]
    
    for i in range(0,cols_7,1):
        if i<0:
            break
        if i >mtx.shape[1]:
            break
        numeros.append(mtx[fila_7][i])
    return numeros
    
arch=open("mapa.txt")
linea=arch.readline().strip()
dimensiones=linea.split()
filas=int(dimensiones[0])
cols=int(dimensiones[1])
mtx=np.zeros([filas,cols])
linea=arch.readline().strip()
posicion_7=[]
fila=0
while linea!="":
    numeros=linea.split()
    for i in range(len(numeros)):    
        mtx[fila][i]=int(numeros[i])
        if int(numeros[i])==7:
            posicion_7.append(fila)
            posicion_7.append(i)
            
    fila+=1
    linea=arch.readline().strip()



print(mtx)
print(posicion_7)
arriba=contar_arriba(mtx, posicion_7)
camino_arriba=identificar_caminos(arriba)[0]
posibilidad_arriba=identificar_caminos(arriba)[1]
suma_arriba=identificar_caminos(arriba)[2]

print(camino_arriba)
print(posibilidad_arriba)
print(suma_arriba)

abajo=contar_abajo(mtx, posicion_7)
camino_abajo=identificar_caminos(abajo)[0]
posibilidad_abajo=identificar_caminos(abajo)[1]
suma_abajo=identificar_caminos(abajo)[2]
print(camino_abajo)
print(posibilidad_abajo)
print(suma_abajo)

izquierda=contar_izquierda(mtx, posicion_7)
camino_izquierda=identificar_caminos(izquierda)[0]
posibilidad_izquierda=identificar_caminos(izquierda)[1]
suma_izquierda=identificar_caminos(izquierda)[2]
print(camino_izquierda)
print(posibilidad_izquierda)
print(suma_izquierda)

derecha=contar_derecha(mtx, posicion_7)
camino_derecha=identificar_caminos(derecha)[0]
posibilidad_derecha=identificar_caminos(derecha)[1]
suma_derecha=identificar_caminos(derecha)[2]
print(camino_derecha)
print(posibilidad_derecha)
print(suma_derecha)

info_suma=[suma_arriba,suma_abajo,suma_izquierda,suma_derecha]
info_posibilidad=[posibilidad_arriba,posibilidad_abajo,posibilidad_izquierda,posibilidad_derecha]
maximo=0
mas_sencillo=0
for i in range(len(info_posibilidad)):
    if info_suma[i]>maximo and info_posibilidad[i]:
        maximo=info_suma[i]
        mas_sencillo=i
if mas_sencillo==0:
    print("arriba")
elif mas_sencillo==1:
    print("abajo")
elif mas_sencillo==2:
    print("izquierda")
elif mas_sencillo==3:
    print("derecha")
    
        
    





