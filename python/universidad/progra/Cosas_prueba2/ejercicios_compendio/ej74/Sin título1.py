import numpy as np
from matplotlib import pyplot as PLT

def mostrarImagen(ancho,alto,r,g,b):
    M=np.dstack((r,g,b))
    # los arrays r g b son ordenados en una matriz indice con indice de cada lista
    #  es decir el indice 0 de los arrays r g b seran incertados en el indice 0 0 de la matriz como lista
    
    PLT.imshow(M)
    PLT.show()
    print(M)
width=15
heigth=15


r=np.random.rand(heigth,width)
# array de 5 elementos randoms
g=np.random.rand(heigth,width)
b=np.random.rand(heigth,width)
mostrarImagen(width, heigth, r, g, b)
