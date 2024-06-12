import numpy as np

def categorias_menores(mtx,categorias):
    promedio_menor=10**10
    for i in range(mtx.shape[0]):
        suma=0
        for j in range(mtx.shape[1]):
            suma+=mtx[i][j]
        promedio=suma/5
        if promedio<promedio_menor:
            promedio_menor=promedio
            maquina=categorias[i]
            fila=i
    print(f"La categoría con menor valor promedio es {maquina} con un valor promedio de {promedio_menor.round(1)}")
    for i in range(mtx.shape[1]):
        print(f"{años[i]} - {mtx[fila][i].round(1)} Millones")   
                


def fecha_2017(mtx):
    for i in range(mtx.shape[1]):
        suma=0 
        for j in range(mtx.shape[0]):
            suma+=mtx[j][i]
    print(f"La valorización final 2027 es de {suma.round(1)}")
    if suma<9500:
        print("El proyecto es conveniente")
    elif suma>=9500:
        print("El proyecto NO es conveniente")

            
    
arch=open("maquinaria.txt","r",encoding="utf-8")
linea=arch.readline()
años=[2023,2024,2025,2026,2027]
categorias=[]
mtx=np.zeros([10,5])

while linea!="":
    partes=linea.split(";")
    categoria_maquina=partes[0]
    fecha=int(partes[1])
    valor_millones=float(partes[2])
    if fecha in años:
        index_año=años.index(fecha)
        
    
    if categoria_maquina not in categorias:
        categorias.append(categoria_maquina)
        mtx[categorias.index(categoria_maquina),index_año]=valor_millones
    elif categoria_maquina in categorias:
         mtx[categorias.index(categoria_maquina),index_año]=valor_millones
    linea=arch.readline().strip()
    
    
categorias_menores(mtx,categorias)
fecha_2017(mtx)
 
 