
import numpy as np
arch=open("texto.txt","r",encoding="utf-8")
linea=arch.readline().strip()
partes=linea.split(",")
filas=int(partes[0])
cols=int(partes[1])
mtx=np.zeros([filas,cols])
mtx2=np.zeros([filas,cols])
n_fila=0
suma=0
linea=arch.readline().strip()
while linea!="":
    numeros=linea.split(",")
    for i in range(len(numeros)):
        suma+=int(numeros[i]) 
        mtx2[n_fila][i]=numeros[i]
        
    
    n_fila+=1
    linea=arch.readline()
        
prom=suma/(filas*cols)
for i in range(mtx.shape[0]):
    for j in range(mtx.shape[1]):
        if mtx2[i][j]>=prom:
            mtx[i][j]=1
print(mtx)



 
    
    
    
    
    
    
    
    
    
    
    