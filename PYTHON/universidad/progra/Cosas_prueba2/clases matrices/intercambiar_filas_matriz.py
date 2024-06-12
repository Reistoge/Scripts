# intercambiar elementos en una matriz
import numpy as np

def intercambiar_filas(mtx,fila1,fila2):
    aux_=tuple(mtx[fila1-1])
    mtx[fila1-1]=(mtx[fila2-1])
    mtx[fila2-1]=aux_
    return mtx



mtx1=np.random.rand(3,3)
print("matriz 1 inicial")
print(mtx1)

#intercambiar fila de matriz: conviertes la variable auxiliar en una tupla para que sea
# inmutable asi no se le asocia la misma direccion que la posicion de la matriz y toma un valor unico
# a=variable auxiliar.
print("matriz 2 nueva")
a=tuple(mtx1[0])
mtx1[0]=mtx1[1]
mtx1[1]=a
print(mtx1)


input()


mtx2=np.random.rand(3,4)
print(mtx2)
mtx2=intercambiar_filas(mtx2, 1, 3)
print(mtx2)

