# ayudantia matrices 
import numpy as np
    
    
    
def sumar_matrices(mtx1,mtx2):
    mtx3=np.zeros([mtx1.shape[0],mtx1.shape[1]])
    for i in range(mtx1.shape[0]):
        for j in range(mtx1.shape[1]):
            mtx3[i][j]=mtx1[i][j]+mtx2[i][j]
    return mtx3

def seleccionar_columna(matriz,n_columna):
    columna=[]
    for i in range(0,matriz.shape[1]):
        columna.append(matriz[i][n_columna])
    return columna
def seleccionar_fila(matriz,n_fila):
    fila=[]
    for i in range(0,matriz.shape[0]):
        fila.append(matriz[n_fila][i])
    return fila
def fila_por_columna(_fila,_columna):
    _suma=0
    for i in range(len(_fila)):
        
        _suma+=_fila[i]*_columna[i]
    return _suma
    
def multiplicar_matrices(mtx1,mtx2):
    mtx3=np.zeros([mtx1.shape[0], mtx2.shape[1]])
    
    for i in range(mtx1.shape[0]):
        
        for j in range(mtx2.shape[1]):
            filas=seleccionar_fila(mtx1, i)
            columnas=seleccionar_columna(mtx2, j)
            mtx3[i][j]=fila_por_columna(filas, columnas)
        
         
    return mtx3
            
            
        
        


def leer_dimensiones(nombre_archivo):
    arch=open(nombre_archivo,encoding="utf-8")
    linea=arch.readline().strip()
    filas=0
    columnas=0
    while linea!="":
        columnas=len(linea.split())
        filas+=1
        linea=arch.readline()
    mtx=np.zeros([filas,columnas])
    arch=open(nombre_archivo,encoding="utf-8")
    linea=arch.readline().strip()
    fila=0
    while linea!="":
        partes=linea.split()
        for i in range(len(partes)):
            mtx[fila][i]=partes[i]
            
        
        fila+=1
        linea=arch.readline().strip()
    return mtx
    


        

operacion=""
while operacion!="salir":
    print("a) multiplicar")
    print("b) sumar")
    print("c) salir")
    while operacion not in ["sumar", "salir","multiplicar"]:
        operacion=input("Que operacion deseas?: ").strip()
        
    if operacion=="salir":
        break   
    
    print("\n"*100)
    print(f"{operacion.capitalize()}")
    arch1=input("ingrese nombre del archivo 1: ").strip()
    arch2=input("ingrese nombre del archivo 2: ").strip()
    mtx1=leer_dimensiones(arch1)
    mtx2=leer_dimensiones(arch2)
    
    while mtx1.shape[0]!=mtx2.shape[0] or mtx1.shape[1]!=mtx2.shape[1]:
        print("las dimensiones de las matrices no son iguales")
        print(f"matriz 1, de {arch1} ")
        print(mtx1)
        print(f"filas {mtx1.shape[0]}")
        print(f"columnas {mtx1.shape[1]} ")
        print(f"matriz 2, de {arch2} ")
        print(mtx2)
        print(f"filas {mtx2.shape[0]}")
        print(f"columnas {mtx2.shape[1]} ")
        print("Edite y guarde los textos asegurandose de que las matrices tengan la mismas dimensiones")
        print(f"un ejemplo seria\n mtx1:\n  {np.random.rand(3,3)} \n mtx2:\n {np.random.rand(3 ,3)}")
        input()
        mtx1=leer_dimensiones(arch1)
        mtx2=leer_dimensiones(arch2)
    print("Dimensiones iguales !")
    print(mtx1)
    print(mtx2)
    if operacion=="sumar":
        print(sumar_matrices(mtx1, mtx2))
    if operacion=="multiplicar":
        print(multiplicar_matrices(mtx1, mtx2))
    input()
        
    
    

mtx1=np.array([[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]])
         
mtx2=np.array([[9, 8, 7],
          [6, 0, 4],
          [3, 2, 1]])


arch=open("matriz 1.txt",encoding="utf-8")
linea=arch.readline().strip()
filas=0
while linea!="":
     
    linea=(linea.split())
    for i in range(0,len(linea),1):
        mtx1[filas][i]=int(linea[i])
    print(mtx1)
    filas+=1
    linea=arch.readline().strip()
 


print(mtx1)

# operacion=""
# while operacion!="salir":
#     print("que operacion deseas ejecutar ?")
#     print("1. suma")
#     print("2. multiplicacion")
    
    