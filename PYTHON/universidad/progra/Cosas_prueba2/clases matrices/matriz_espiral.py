
import numpy as np
espiral=[]



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