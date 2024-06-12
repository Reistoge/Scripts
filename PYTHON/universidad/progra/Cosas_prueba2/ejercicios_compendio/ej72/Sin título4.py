import numpy as np

arch=open("tecto.txt","r",encoding="utf-8")
mtx=np.zeros([26,26])
letras=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 
linea=arch.readline().strip()
while linea!="":
    partes=linea.split(",")
    fila=partes[0].strip()
    columna=partes[1].strip()
    valor=int(partes[2])
    mtx[letras.index(fila)][letras.index(columna)]+=valor
        
        
    linea=arch.readline().strip()
mayor=0
menor=10**10
posiciones_mayor=[]
posiciones_menor=[]
for i in range(len(mtx)):
    for j in range(len(mtx[0])):
        if mtx[i][j]==mayor:
            posiciones_mayor.append([i,j])
        if mtx[i][j]==menor:
             posiciones_menor.append([i,j])
        if mtx[i][j]>mayor:
            mayor=mtx[i][j]
            posiciones_mayor.clear()
            posicion=[i,j]
            posiciones_mayor.append(posicion)
        if mtx[i][j]<menor and mtx[i][j]>0 :
             menor=mtx[i][j]
             posiciones_menor.clear()
             posicion=[i,j]
             posiciones_menor.append(posicion)
                 

                
print(mayor)
for i in range(len(posiciones_mayor)):
    print(f"en {letras[posiciones_mayor[i][0]]} {letras[posiciones_mayor[i][1]]}")
print()
print(menor) 
for i in range(len(posiciones_menor)):
    print(f"en {letras[posiciones_menor[i][0]]} {letras[posiciones_menor[i][1]]}")
 
