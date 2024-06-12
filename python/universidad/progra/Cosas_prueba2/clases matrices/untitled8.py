import numpy as np
espiral=[]

def buscar_agregar(lista,elemento):
    if elemento not in lista:
        lista.append(elemento)
    return lista.index(elemento)
def intercambiar(lista,i,j):
    aux=lista[i]
    lista[i]=lista[j]
    lista[j]=aux
 
    
def intercambiar_columna_matriz(mtx,nombre1,nombre2):
    indice_columna1=personas.index(nombre1)
    indice_columna2=personas.index(nombre2)
    for i in range(0,len(mtx)):
        aux=mtx[i][indice_columna2]
        mtx[i][indice_columna2]=mtx[i][indice_columna1]
        mtx[i][indice_columna1]=aux
        
def intercambiar_filas_matriz(mtx,i,j):
    aux=tuple(mtx[i])
    mtx[i]=mtx[j]
    mtx[j]=aux
    
def contar_derecha(mtx,fila,columna_inicio,columna_final):
    if columna_inicio>=0 and columna_final>=0:
        for i in range(columna_inicio,columna_final,1):
            print(mtx[fila][i])
            espiral.append(mtx[fila][i])
def contar_abajo(mtx,columna,fila_inicio,fila_final):
    if fila_inicio>=0 and fila_final>=0:
        for i in range(fila_inicio,fila_final,1):
            print(mtx[i][columna])
            espiral.append(mtx[i][columna])
        
def contar_izquierda(mtx,fila,columna_inicio,columna_final):
    if columna_inicio>=0 and columna_final>=0:
        for i in range(columna_inicio,columna_final,-1):
            print(mtx[fila][i])
            espiral.append(mtx[fila][i])
        
def contar_arriba(mtx,columna,fila_inicio,fila_final):
    if fila_inicio>=0 and fila_final>=0:
        for i in range(fila_inicio,fila_final,-1):
            print(mtx[i][columna])
            espiral.append(mtx[i][columna])
        
    

arch=open("maquinas.txt",encoding="utf-8")
linea=arch.readline()

personas=[]
maquinas=[]
dist_totales=[]
mtx=np.zeros([8,5])
while linea!="":
    partes=linea.split(";")
    nombre=partes[0]
    maquina=partes[1]
    kilometros=int(partes[2])
    
    fila=buscar_agregar(maquinas, maquina)
    columna=buscar_agregar(personas, nombre)
    mtx[fila][columna]=+kilometros
    
    
    

    linea=arch.readline()
print(mtx)    

for i in range(len(personas)):
    suma=0
    for j in range(len(maquinas)):
        suma+=mtx[j][i]
    dist_totales.append(suma)
print(dist_totales)

for i in range(len(dist_totales)-1):
    for j in range(i+1,len(dist_totales),1):
        if dist_totales[i]<dist_totales[j]:
            intercambiar(dist_totales, i, j)
            intercambiar(personas, i, j)
            intercambiar_columna_matriz(mtx, personas[i], personas[j])


print("\n\nOrdenado mayor uso por trabajador")
print(mtx)
print(dist_totales)
            



maquinas_suma=[]
for i in range(len(maquinas)):
    suma=0
    for j in range(len(personas)):
        suma+=mtx[i][j]
    maquinas_suma.append(suma)
print(maquinas_suma)


print("\n\nOrdenado mayor uso por trabajador y mayor uso de maquina")
for i in range(len(maquinas_suma)-1):
    for j in range(i+1,len(maquinas_suma),1):
        if maquinas_suma[i]<maquinas_suma[j]:
            intercambiar(maquinas, i, j)
            intercambiar(maquinas_suma,i,j)
            intercambiar_filas_matriz(mtx, i, j)

print(mtx)
print(dist_totales)

for i in range(mtx.shape[0]):
    for j in range(mtx.shape[1]):
        print(mtx[i][j],end=" ")
    print(f"|{maquinas_suma[i]}")


mtx=np.array([[ 1,   2,  3, 4 ],
               [12, 13, 14, 5],
               [11, 16, 15, 6],
               [10, 9, 8,   7  ]])
mtx2=np.array([10, 9, 8])


mtx=np.array([[1, 2, 3, 4, 5,   6,     7],
              [24, 25, 26, 27, 28, 29, 8],
              [23, 40, 41, 42, 43, 30, 9],
              [22, 39, 48, 49, 44, 31, 10],
              [21, 38, 47, 46, 45, 32, 11],
              [20, 37, 36, 35, 34, 33, 12],
              [19, 18, 17, 16, 15, 14, 13]])
mtx4=np.array([[1, 1, 3],
              [2, 0, 0]])



print("\n\n\n")
F=mtx.shape[0]-1
C=mtx.shape[1]-1

A=0
B=0
elements=F*C
while A!=F and B!=C:
        
        contar_derecha(mtx,A , B, C)
        contar_abajo(mtx, C, A, F)        
        contar_izquierda(mtx, F, C, B )
        contar_arriba(mtx, B, F, A)
        C-=1
        F-=1
        A+=1
        B+=1
   
        if F<=0 or C<=0:
            break
        
        if B==C or A==F:
            contar_derecha(mtx,A , B, C+1)
            break
        
            

print(espiral)
      
        
        
        
        
        
        
        
        
        
         
   
    
   
    
    
        

    
    



            
 
    

 

          
          

          
          
          
          
          
          
          
          