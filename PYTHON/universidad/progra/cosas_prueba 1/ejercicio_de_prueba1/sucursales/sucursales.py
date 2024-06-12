arch=open("problema1.txt","r")
sucursales=[]
T=int(arch.readline())
total_de_ventas=0
precio_caro=0
producto_caro=""
sucursal_del_producto_caro=""
while T>0:
    sucursal,cantidad_de_productos=arch.readline().split(",")
    
    unidades_totales=0
    unidades_unitarias_de_sucursal=0
    total_mayor=0
    venta_de_sucursal=0
    cantidad_de_productos=int(cantidad_de_productos)
    #porque hay que dejar aqui esta variable ?? y no adentro del for??
    cantidad_de_producto_mayor=0
    
    for i in range(0,cantidad_de_productos,1):
        nombre_del_producto,cantidad_vendida,precio_unitario=arch.readline().split(",")
            
        #spliteamos cada variable por linea de codigo
        cantidad_vendida=int(cantidad_vendida)
        precio_unitario=int(precio_unitario)
        if cantidad_vendida==1:
            unidades_unitarias_de_sucursal=unidades_unitarias_de_sucursal+1
        #checkeamos si la cantidad vendida es 1
        
        
        unidades_totales+=cantidad_vendida
        total_del_producto=cantidad_vendida*precio_unitario  
        venta_de_sucursal+=cantidad_vendida*precio_unitario  
        total_de_ventas+=cantidad_vendida*precio_unitario
        if total_del_producto>=total_mayor:
            
            #guardamos la variable mayor
            total_mayor=total_del_producto
            #se registra el nombre del producto
            producto_mayor=nombre_del_producto
            #guardamos la cantidad en la que se vendio ese el producto más vendido
            cantidad_de_producto_mayor=cantidad_vendida
            sucursal_del_producto_caro=sucursal
            
            
        if precio_unitario>=precio_caro:
            precio_caro=precio_unitario
            producto_caro=nombre_del_producto
            
            
            
    
    sucursales.append(producto_mayor)
    sucursales.append(total_mayor)
    sucursales.append(cantidad_de_producto_mayor)
    sucursales.append(unidades_totales)
    sucursales.append(venta_de_sucursal)

    
    if cantidad_de_productos==0:
        print("No hubo ventas en la sucursal", sucursal)
        
    elif cantidad_de_productos!=0:
        print("Producto con mayor venta en sucursal: "+sucursal)
        print("es "+producto_mayor+ " con total "+str(total_mayor))
        print("porcentaje de ventas unitarias es: ", 100*unidades_unitarias_de_sucursal/cantidad_de_productos)
    
    T-=1
    
        
    
print("Total de ventas: "+str(total_de_ventas))
print("El producto más caro fue", producto_caro)
print("vendido en la sucursal",sucursal_del_producto_caro)
print("con un precio de",precio_caro)



