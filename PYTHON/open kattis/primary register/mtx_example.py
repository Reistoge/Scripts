import numpy as np
mtx=np.random.rand(3,3)
print(mtx)
#intercambiar fila de matriz: conviertes la variable auxiliar en una tupla para que sea
# inmutable asi no se le asocia la misma direccion que la posicion de la matriz y toma un valor unico
# a=variable auxiliar.
a=tuple(mtx[0])
mtx[0]=mtx[1]
mtx[1]=a


print(mtx)