import numpy as np

def checkear_columna(mtx,col):
    columna=int(col)-1
    cont1=0
    cont2=0
    
    valida=True
    for fila in range(mtx.shape[1]):
        if mtx[fila][columna]==1:
            cont1+=1
        elif mtx[fila][columna]==2:
            cont2+=1
    print(cont1+cont2)
    if abs(cont1-cont2)>=2 or (cont1+cont2)==dim:
        valida=False
        if columna<=mtx.shape[1] and columna not in cols_eliminadas:
            cols_eliminadas.append(columna)
    
    return [valida,mtx.shape[1]-(cont1+cont2)]
        
    
    
        
    
    
        
            
def cargar_juego(dim ,inicio,movidas):
    dim=int(dim)
    mtx=np.zeros([int(dim),int(dim)])
    jugadas1=[]
    jugadas2=[]
    if inicio=="1":
        for i in range(len(movidas)):
            if i%2==0:
                jugadas1.append(int(movidas[i]))
                if int(movidas[i])>dim:
                    print(f"Movida invalida jugador 1 en indice {int(movidas[i])-1}")
                elif int(movidas[i])<=dim:
                    columna_valida=checkear_columna(mtx,int(movidas[i]))[0]
                    fila=checkear_columna(mtx,movidas[i])[1]
                    if columna_valida:
                        mtx[fila-1][int(movidas[i])-1]=1
                        checkear_columna(mtx, movidas[i])
                        print(mtx)
                        
                    elif columna_valida==False:
                        if int(movidas[i]) not in cols_eliminadas:
                            cols_eliminadas.append(int(movidas[i]))
                        print(f"Movida invalida jugador 1 en indice {int(movidas[i])-1}") 
            elif i%2!=0:
                jugadas2.append(int(movidas[i]))
                if int(movidas[i])>dim:
                    print(f"Movida invalida jugador 2 en indice {int(movidas[i])-1}")
                elif int(movidas[i])<=dim:
                    columna_valida=checkear_columna(mtx,int(movidas[i]))[0]
                    fila=checkear_columna(mtx,movidas[i])[1]
                    if columna_valida:
                        mtx[fila-1][int(movidas[i])-1]=2
                        checkear_columna(mtx, movidas[i])
                        print(mtx)
                    elif columna_valida==False:
                        if int(movidas[i]) not in cols_eliminadas:
                            cols_eliminadas.append(int(movidas[i]))
                        print(f"Movida invalida jugador 2 en indice {int(movidas[i])-1}")
                        
            
            print(cols_eliminadas)
            
            
    elif inicio=="2":
        for i in range(len(movidas)):
            if i%2==0:
                jugadas2.append(int(movidas[i]))
                if int(movidas[i])>dim:
                    print(f"Movida invalida jugador 2 en indice {int(movidas[i])-1}")

            else:
                jugadas1.append(int(movidas[i]))
                if int(movidas[i])>dim:
                    print(f"Movida invalida jugador 1 en indice {int(movidas[i])-1}")
    
    
                
    
        
            
arch=open("movidas.txt","r",encoding="utf-8")
linea=arch.readline()
juegos=0
while linea!="":
    cols_eliminadas=[]
    partes=linea.split()
    dim=partes[0]
    inicio=partes[1]
    movidas=partes[2:-1]
    print(juegos)
    cargar_juego(dim, inicio, movidas)
    
    linea=arch.readline()
    juegos+=1

