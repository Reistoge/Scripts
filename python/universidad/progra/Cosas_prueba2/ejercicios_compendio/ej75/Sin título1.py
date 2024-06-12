import numpy as np
from matplotlib import pyplot as PLT
def difuminado(matriz,cantidad):
    
    suma=0
    for i in range(0,len(matriz),1):
       
        suma+=cantidad
        for j in range(len(matriz[0])):
            matriz[i][j]=suma
    mostrarImagen(width, heigth, r, g, b)



def mostrarImagen(ancho,alto,r,g,b):
    M=np.dstack((r,g,b))
    # los arrays r g b son ordenados en una matriz indice con indice de cada lista
    #  es decir el indice 0 de los arrays r g b seran incertados en el indice 0 0 de la matriz como lista
    
    PLT.imshow(M)
    PLT.show()
    print(M)
width=10
heigth=10

# while True:
#     r=np.random.rand(heigth,width)
#     # array de 5 elementos randoms
#     g=np.random.rand(heigth,width)
#     b=np.random.rand(heigth,width)
#     mostrarImagen(width, heigth, r, g, b)

r=np.zeros([heigth,width])
g=np.zeros([heigth,width])
b=np.zeros([heigth,width])
cont_dif=0
for i in range(0,100,1):
    cont_dif+=0.001
    difuminado(b,cont_dif)
cont_dif=0
for i in range(0,50,1):
    cont_dif+=0.001
    difuminado(r,cont_dif)
 


# array de 5 elementos randoms
 
