import numpy as np

def mayor_matriz(matriz):
    mayor=0
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            if matriz[i][j]>mayor:
                mayor=matriz[i][j]
    return mayor
            
def aislar(centro,fila,columna,mtx):
     
    bloque=np.zeros([3,3])
    fila_bloque=0
    columna_bloque=0
    
    for i in range(fila-1,fila+2,1):
        if i<0:
            fila_bloque+=1
            continue
        elif i>=mtx.shape[0]:
            break
        columna_bloque=0
        for j in range(columna-1,columna+2,1):
            if j<0:
                columna_bloque+=1
                continue
            elif j>=mtx.shape[1]:
                break
            bloque[fila_bloque][columna_bloque]=mtx[i][j]
            
            columna_bloque+=1
        fila_bloque+=1
    return bloque
            
            
        
        
    
arch=open("texto.txt","r",encoding="utf-8")
linea=arch.readline().strip()
filas=int(linea.split(",")[0])
cols=int(linea.split(",")[1])
mtx=np.zeros([filas,cols])
linea=arch.readline().strip()
for i in range(filas):
    
    numeros=linea.split(",")
    for j in range(len(numeros)):
        mtx[i][j]=int(numeros[j].strip())

    linea=arch.readline().strip()
 
mtx2=np.zeros([filas,cols])    
for i in range(mtx.shape[0]):
    for j in range(mtx.shape[1]):        
       mtx2[i][j]=mayor_matriz(aislar(mtx[i][j], i, j, mtx))
             
print(mtx2)
              
 
              
mtx3=np.random.rand(10,10)
for i in range(mtx3.shape[0]):
    for j in range(mtx3.shape[1]):
        print(aislar(mtx3[i][j],i,j,mtx3))
 
 
              
 
              
 
              
 
              
 
              
 
              
 
              
 
              
 
              
 
              
 
              
 
              
 
              
 
              
 
              
 