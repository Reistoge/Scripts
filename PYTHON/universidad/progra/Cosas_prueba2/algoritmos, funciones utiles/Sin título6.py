import numpy as np
def aislar(centro,fila,columna,mtx):
     
    bloque=np.zeros([3,3])
    fila_bloque=0
    columna_bloque=0
    for i in range(fila-1,fila+2,1):
        # si la fila fuese 0, el for seria -1, 0, 1... es un for(-1,2,1)
        if i<0:
            # si la fila no existe, nos saltamos la fila
            fila_bloque+=1
            continue
        elif i>=mtx.shape[0]:
            # si nos pasamos de fila paramos la funcion
            break
        columna_bloque=0
        for j in range(columna-1,columna+2,1):
            if j<0:
                # si la columna no existe pasamos a la siguiente columna
                columna_bloque+=1
                continue
            elif j>=mtx.shape[1]:
                # si nos pasamos de columna paramos el programa
                break
            
            
            # si el elemento existe y esta a 1 distancia 
            # manhattan lo guardamos respecto a la posicion 
            # del elemento del centro.
            bloque[fila_bloque][columna_bloque]=mtx[i][j]
            
            columna_bloque+=1
            # seguimos a la siguiente columna a guardar en el bloque
            
        
        fila_bloque+=1
        # despues de guardar los elementos de esa fila que existian o no pasamos a la siguiente fila.
    return bloque
def ordenar_matriz_respecto_fila(mtx,lista):
    def intercambiar(lista,i,j):
        aux=lista[i]
        lista[i]=lista[j]
        lista[j]=aux
    def intercambiar_filas(mtx,fila1,fila2):
        for i in range(0,mtx.shape[0],1):
            for j in range(0,mtx.shape[1],1):
                # en este caso como queremos mover las filas nuestro pivote 
                # estara en la segunda casilla queremos movernos dentro de cada fila
                # dejamos estatico las filas ya que esa es la queremos y movemos cada elemento de esa fila.
                # que quieres cambiar? las filas, que quieres mover? cada elemento de esa fila respecto a otra
                aux=mtx[fila1][j]
                mtx[fila1][j]=mtx[fila2][j]
                mtx[fila2][j]=aux
        
    for i in range(0,len(lista),1):
        for j in range(i+1,len(lista),1):
            if lista[i]>lista[j]:
                intercambiar(lista, i, j)
                intercambiar_filas(mtx, i, j)
def ordenar_matriz_respecto_col(mtx,lista):
    def intercambiar(lista,i,j):
        aux=lista[i]
        lista[i]=lista[j]
        lista[j]=aux
    def intercambiar_col(mtx,col1,col2):
        for i in range(0,mtx.shape[1],1):
            for j in range(0,mtx.shape[0],1):
                # como queremos cambiar nuestras cols nuestro pivote estara en las filas estando estatico nuestro elemento de la columna 
                # ya que queremos ir bajando por cada fila pero dejando estatico en la columna el cual esta
                # que quieres cambiar? las columnas, que quieres mover? cada elemento de esa columna respecto a otra
                aux=mtx[j][col1]
                mtx[j][col1]=mtx[j][col2]
                mtx[j][col2]=aux
        
    for i in range(0,len(lista),1):
        for j in range(i+1,len(lista),1):
            if lista[i]>lista[j]:
                intercambiar(lista, i, j)
                intercambiar_col(mtx, i, j)
                
                

lista_mtx=np.random.rand(15)   
mtx_ex=np.random.rand(3,15)


    
  
    