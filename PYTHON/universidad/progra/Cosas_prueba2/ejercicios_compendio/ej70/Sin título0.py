import numpy as np
def intercambiar(lista,i,j):
    aux=lista[i]
    lista[i]=lista[j]
    lista[j]=aux    
        
def existe_bodega(bodega):
    suma=0
    for i in range(len(bodega)):
        suma+=bodega[i]
    if suma>0:
        return True
    else:
        return False
def ordenar_lista(lista,lista2,lista3):
    for i in range(len(lista)):
        for j in  range(i+1,len(lista)):
            if lista[i]>lista[j]:
                intercambiar(lista, i, j)
                intercambiar(lista2, i, j)
                intercambiar(lista3, i, j)
    
        
def formatear_bodega(bodega,n_bodega):
    productos_formateados=[]
    stocks_formateados=[]
    valores_formateados=[]
    for i in range(len(bodega)):
        if bodega[i]>0:
            stocks_formateados.append(mtx_stock[n_bodega][i])
            valores_formateados.append(mtx_vu[n_bodega][i])
            productos_formateados.append(productos[i])
   
    ordenar_lista(valores_formateados,productos_formateados,stocks_formateados)
    for i in range(len(valores_formateados)):
        print(f"{productos_formateados[i]}: {stocks_formateados[i]} {valores_formateados[i]}")
            
    
 
     
   
#ej 70
# código_bodega,código_producto,stock,valor_unitario
# matriz1(stock)
# fila = bodegas 
# columnas= codigo producto
#  casilla= stock

# matriz2(valor unitario): 
# # matriz1
# fila = bodegas 
# columnas= codigo producto
#  casilla= valor unitario 

productos=[]
mtx_stock=np.zeros([50,50])
mtx_vu=np.zeros([50,50])

# 1. Total valorizado en las bodegas, 
# 2. Total valorizado por bodega
# 3. Código del producto menos valorizado por cada bodega
# 4. Lista de productos que tienen stock superior a 1000 por bodega
# 5. Promedio total de productos valorizado
# 6. Promedio total de productos valorizado por bodega
# 7. Código y precio unitario del producto más barato por bodega
# 8. Listado, por bodega, y ordenado por precio unitario, de menor a mayor, de todos los productos
# voy a ingresar los datos en la mtx, despues voy a sumar todos los valores unitarios
# para el total valorizado por bodega sumare todos los 
# 
total_valorizado=0

arch=open("bodegas.txt","r",encoding="utf-8")

linea=arch.readline().strip()
while linea!="":
    partes=linea.split(",")
    bodega=partes[0]
    codigo_bodega=int(bodega.split()[1])-1
    codigo_producto=partes[1].strip()
    stock=int(partes[2])
    valor_unitario=int(partes[3])
    total_valorizado+=stock*valor_unitario
    if codigo_producto not in productos:
        productos.append(codigo_producto)
        mtx_stock[codigo_bodega][productos.index(codigo_producto)]+=stock
        mtx_vu[codigo_bodega][productos.index(codigo_producto)]=valor_unitario
    elif codigo_producto in productos:
        mtx_stock[codigo_bodega][productos.index(codigo_producto)]+=stock
        mtx_vu[codigo_bodega][productos.index(codigo_producto)]=valor_unitario

    linea=arch.readline().strip()

# total
total_por_bodega=[]
for i in range(mtx_stock.shape[0]):
    suma_por_bodega=0
    for j in range(mtx_stock.shape[1]):
        suma_por_bodega+=mtx_stock[i][j]*mtx_vu[i][j]
    total_por_bodega.append(suma_por_bodega)

# menor de vu

            
            
        
        
    
print(mtx_stock)
print(mtx_vu)
print(productos)
print(f"A. {total_valorizado}")



print(f"")
for i in range(len(total_por_bodega)):
        if total_por_bodega[i]>0:    
            print(f"B. bodega {i+1}: {total_por_bodega[i]}")
        
print()
for i in range(mtx_vu.shape[0]):
    menor=10**10
    producto_menor=""
    
    for j in range(mtx_vu.shape[1]):
      if mtx_vu[i][j]<menor and mtx_vu[i][j]>0:
            menor=mtx_vu[i][j]*mtx_stock[i][j]
            producto_menor=productos[j]
    if menor<10**10:    
        print(f"C. bodega {i+1} {producto_menor}, {menor}")
    
    
print()
numero_bodegas=1            
for i in range(mtx_stock.shape[0]):
    productos_mayores_a_mil_stock=""
    suma=0
    for j in range(mtx_stock.shape[1]):
        suma+=mtx_stock[i][j]
        if mtx_stock[i][j]>1000:
            productos_mayores_a_mil_stock+=" "+productos[j]
        
    if suma>0:
        numero_bodegas+=1
        print(f"D. bodega {i+1}: {productos_mayores_a_mil_stock} ")
        

# valorizado por bodega
print()

for i in range(mtx_vu.shape[0]):
    
    producto=0
    for j in range(mtx_vu.shape[1]):
        if mtx_stock[i][j]>0:
            producto+=1
    if total_por_bodega[i]>0:    
        print(f"F. bodega {i+1}: {(total_por_bodega[i]/producto)}")
        
suma_prom=0
for i in range(mtx_vu.shape[0]):
    
    producto=0
    for j in range(mtx_vu.shape[1]):
        if mtx_stock[i][j]>0:
            producto+=1
    if producto>0:    
        suma_prom+=total_por_bodega[i]/producto
print()
print(suma_prom/(len(productos)-1))
    
print()
for i in range(mtx_vu.shape[0]):
    menor=10**10
    producto_menor=""
    
    for j in range(mtx_vu.shape[1]):
      if mtx_vu[i][j]<menor and mtx_vu[i][j]>0:
            menor=mtx_vu[i][j]
            producto_menor=productos[j]
    if menor<10**10:    
        print(f"G. bodega {i+1} {producto_menor}, {menor}")
    

    
print()

for i in range(mtx_stock.shape[0]):
    if(existe_bodega(mtx_stock[i])):
        print(f"Bodega {i+1}")
        formatear_bodega(mtx_stock[i], i)
        print()
        
        
        
        
    

        







    