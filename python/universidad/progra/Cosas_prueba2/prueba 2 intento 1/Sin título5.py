import numpy as np
def menor_columna(mtx1,mtx2,mtx3):
    menor=10**10
    for cols in range(mtx1.shape[1]):
        sku_menor=""
        producto_menor=""
        menor=10**10
        for fila in range(mtx1.shape[0]):
            if mtx1[fila][cols]!=0:
                if mtx1[fila][cols]<menor:
                    menor=mtx1[fila][cols]
                    sku_menor=skus[fila]
                    producto_menor=nombres[fila]
        for fila in range(mtx1.shape[0]):
            if mtx2[fila][cols]!=0:
                if mtx2[fila][cols]<menor:
                    menor=mtx2[fila][cols]
                    sku_menor=skus[fila]
                    producto_menor=nombres[fila]
        for fila in range(mtx1.shape[0]):
            if mtx3[fila][cols]!=0:
                if mtx3[fila][cols]<menor:
                    menor=mtx3[fila][cols]
                    sku_menor=skus[fila]
                    producto_menor=nombres[fila]
         
        if cols>=len(categorias):
            break
        print(sku_menor,producto_menor,menor)
def precio_oferta_menor(mtx_normal,mtx):
    mayor=0
    producto=""
    sku=""
    for i in range(mtx.shape[0]):
        for j in range(mtx.shape[1]):
            if mtx_normal[i][j]!=0 and mtx[i][j]!=0:
                if ((mtx_normal[i][j]-mtx[i][j])*100/mtx_normal[i][j])>mayor:
                    mayor=((mtx_normal[i][j]-mtx[i][j])/mtx_normal[i][j])*100
                    producto=nombres[i]
                    sku=skus[i]
    print(sku,producto,mayor)
    
    
    
arch=open("Productos.txt","r",encoding="utf-8")
linea=arch.readline().strip()               
nombres=[]
skus=[]
categorias=[]
mtx_normal=np.zeros([600,600])
mtx_f=np.zeros([600,600])
mtx_p=np.zeros([600,600])
mtx_r=np.zeros([600,600])
while linea!="":
    partes=linea.split(";")
    sku=int(partes[0])
    nombre=partes[1]
    categoria=(partes[2])
    precio=float(partes[3])
    precio_f=float(partes[4])
    precio_r=float(partes[5])
    precio_p=float(partes[6])
    if sku not in skus:
        skus.append(sku)
        nombres.append(nombre)
    if categoria not in categorias:
        categorias.append(categoria)  
    mtx_normal[skus.index(sku)][categorias.index(categoria)]=precio
    mtx_f[skus.index(sku)][categorias.index(categoria)]=precio_f
    mtx_p[skus.index(sku)][categorias.index(categoria)]=precio_p
    mtx_r[skus.index(sku)][categorias.index(categoria)]=precio_r
    linea=arch.readline().strip()


menor_columna(mtx_f,mtx_p,mtx_r)
print()
precio_oferta_menor(mtx_normal, mtx_f)
print()
precio_oferta_menor(mtx_normal, mtx_r)
print()
precio_oferta_menor(mtx_normal, mtx_p)


print(mtx_f[skus.index(5)])
# arch2=open("Boletas.txt","r",encoding="utf-8")
# linea=arch2.readline()
# while linea!="":
#     print()
#     linea=arch2.readline()


 