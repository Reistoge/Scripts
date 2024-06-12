import numpy as np
def lista_a_int(lista):
    for i in range(len(lista)):
        lista[i]=int(lista[i])-1
    return lista
def copiar_matriz(matriz1):
    mtx2=np.zeros([dim,dim])
    for i in range(matriz1.shape[0]):
        for j in range(matriz1.shape[1]):
            mtx2[i][j]==matriz1[i][j]
    return mtx2
def check_columna_valida(mtx,col_movida):
    cont1=0
    cont2=0
    ultimo=0
    pos_pieza=0
    valida=True
    for i in range(mtx.shape[0]):
        if mtx[i][col_movida]==0:
            pos_pieza+=1
        if mtx[i][col_movida]==1:
            cont1+=1
        elif mtx[i][col_movida]==2:
            cont2+=1        
        ultimo=mtx[i][col_movida]
    
    if (cont1+cont2)==mtx.shape[0]:        
        # se lleno
        valida=False
        if col_movida not in cols_eliminadas:
            cols_eliminadas.append(col_movida)
             
        if len(cols_eliminadas)<=mtx.shape[1]:
            for i in range(mtx.shape[0]):
                mtx[i][col_movida]=0
            cols_eliminadas.remove(col_movida)
            valida=True
        if len(cols_eliminadas)==mtx.shape[0]-1:
            
            return -1
        
        
    elif abs(cont1-cont2)>=2 :
        valida=False
        if col_movida not in cols_eliminadas:
            cols_eliminadas.append(col_movida)
        # eliminar esa columna
     
    return [valida,pos_pieza]

        
def cargar_juego(dim,inicio,movidas):
    mtx=np.zeros([dim,dim])
    print(mtx)
    jugador1=[]
    jugador2=[]
    
    if inicio==1:
        
        for i in range(len(movidas)):
            
            if i%2==0:
                if movidas[i]>=dim:
                    print(f" Movida inválida jugador 1 índice {movidas[i]}")
                elif movidas[i]<dim:
                     retornos=check_columna_valida(mtx, movidas[i])
                     if retornos==-1:
                         return print("ganador 1")
                     columna_valida=retornos[0]
                     pos_pieza=retornos[1]
                     if columna_valida:
                         mtx[pos_pieza-1][movidas[i]]=1
                         if check_columna_valida(mtx, movidas[i])==-1:
                             return print("ganador 1")
                         
                          
                             
                           
                     elif columna_valida==False:
                        print(f" Movida inválida jugador 1 índice {movidas[i]}")
            elif i%2!=0:
                if movidas[i]>=dim:
                    print(f" Movida inválida jugador 2 índice {movidas[i]}")
                
                elif movidas[i]<dim:
                     retornos=check_columna_valida(mtx, movidas[i])
                     if retornos==-1:
                         return print("ganador 2")
                     columna_valida=retornos[0]
                     pos_pieza=retornos[1]
                     if columna_valida:
                         mtx[pos_pieza-1][movidas[i]]=2
                         if check_columna_valida(mtx, movidas[i])==-1:
                             return print("ganador 2")
                     elif columna_valida==False:
                         print(f" Movida inválida jugador 2 índice {movidas[i]}")
        ultimo=mtx[pos_pieza-1][movidas[i]]
            
    
    elif inicio==2:
        for i in range(len(movidas)):
            
            if i%2==0:
                if movidas[i]>=dim:
                    print(f" Movida inválida jugador 2 índice {movidas[i]}")
                
                elif movidas[i]<dim:
                      
                     retornos=check_columna_valida(mtx, movidas[i])
                     if retornos==-1:
                         return print("ganador 2")
                     columna_valida=retornos[0]
                     pos_pieza=retornos[1]
                     if columna_valida:
                         mtx[pos_pieza-1][movidas[i]]=2
                     elif columna_valida==False:
                        print(f" Movida inválida jugador 2 índice {movidas[i]}")       
            elif i%2!=0:
                
                if movidas[i]>=dim:
                    print(f" Movida inválida jugador 1 índice {movidas[i]}")
                
                elif movidas[i]<dim:
                      

                     retornos=check_columna_valida(mtx, movidas[i])
                     if retornos==-1:
                         return print("ganador 1")
                     columna_valida=retornos[0]
                     pos_pieza=retornos[1]
                     if columna_valida:
                         mtx[pos_pieza-1][movidas[i]]=1
                     elif columna_valida==False:
                         print(f" Movida inválida jugador 1 índice {movidas[i]}")
        ultimo=(mtx[pos_pieza-1][movidas[i]])
         
             
    if ultimo!=0:
        print(f"ganador {ultimo}")
    if ultimo==0:
        print("no hay ganador")
    
arch=open("movidas.txt","r",encoding="utf-8")
linea=arch.readline().strip()

while linea!="":
    cols_eliminadas=[]
    partes=linea.split()
    dim=int(partes[0])
    inicio=int(partes[1])
    
    movidas=partes[2:len(partes)]
    lista_a_int(movidas)
    print(dim,inicio,movidas)
    cargar_juego(dim,inicio,movidas)
    
    linea=arch.readline().strip()
    print()
