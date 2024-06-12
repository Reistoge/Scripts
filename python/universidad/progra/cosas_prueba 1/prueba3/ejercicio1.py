
nombre_producto=""
utiles=0
producto_costoso=""
precio_costoso=0

producto_menor_desc=""
precio_precio_menor_desc=0

producto_tienda_comparada=""
mayor_cantidad_comparada=0

menor_descuento=2

while nombre_producto !="FIN":
    
    nombre_producto=input("Ingrese el nombre del producto (FIN para terminar): ").upper()
    
    if nombre_producto=="FIN":
        break
    utiles+=1
    tipo_producto=input("Ingrese el tipo de producto (ELECTRÓNICA,ROPA,MUEBLE):").upper()
    while tipo_producto not in ["ELECTRÓNICA","ROPA","MUEBLE"]:
        tipo_producto=input("Ingrese el tipo de producto (ELECTRÓNICA,ROPA,MUEBLE):").upper()
        
    precio_producto=int(input("Ingrese el precio normal del producto: "))
    while precio_producto<=0:
        precio_producto=int(input("Ingrese el precio normal del producto: "))
        
    if precio_producto>precio_costoso:
        precio_costoso=precio_producto
        producto_costoso=nombre_producto
        
    cantidad_productos=int(input("Ingrese la cantidad de tiendas a comparar: "))
    while cantidad_productos<=0:
        cantidad_productos=int(input("Ingrese la cantidad de tiendas a comparar: "))
    if cantidad_productos>mayor_cantidad_comparada:
        mayor_cantidad_comparada=cantidad_productos
        producto_tienda_comparada=nombre_producto
        
    suma_precios=0
    for i in range(0, cantidad_productos,1):
        
        precio_visto=int(input(f"Ingrese el precio visto en la tienda {i+1}: "))
        while precio_visto<=0:
            precio_visto=int(input(f"Ingrese el precio visto en la tienda {i+1}: "))
        
        suma_precios+=precio_visto
        
        precio_promedio=suma_precios/cantidad_productos
    
    descuento=0
    precio_sugerido=0
    if precio_promedio > precio_producto:
        if tipo_producto=="ROPA":
            descuento=0.2
            precio_sugerido=round(precio_producto*0.8)
            
        elif tipo_producto=="ELECTRÓNICA":
            descuento=0.05
            precio_sugerido=round(precio_producto*0.95)
            
        elif tipo_producto=="MUEBLE":
            descuento=0.1
            precio_sugerido=round(precio_producto*0.9)
            
    elif precio_promedio<=precio_producto:
        precio_sugerido=round(precio_promedio*0.95)
        descuento=1-(precio_sugerido/precio_producto)
    if descuento<menor_descuento:
        menor_descuento=descuento
        producto_menor_desc=nombre_producto
        
        
            
    print(f"PRECIO OFERTA SUGERIDO: {precio_sugerido}")
    print(f"DESCUENTO: {descuento}%")
    if (tipo_producto=="ROPA" and descuento>0.8) or (tipo_producto=="ELECTRÓNICA" and descuento > 0.3) or (tipo_producto=="MUEBLE" and descuento>0.5):
       print("NO VALE LA PENA OFRECER ESTE PRODUCTO EN EL EVENTO")
       utiles-=1
         
       
print(f"PRODUCTO MAS COSTOSO INGRESADO: {producto_costoso}")
print(f"PRODUCTO CON MENOR DESCUENTO: {producto_menor_desc}")
print(f"PRODUCTO CON MAS TIENDAS COMPARADAS: {producto_tienda_comparada}")
print(f"CANTIDAD DE PRODUCTOS UTILES PARA EL EVENTO: {utiles}")

        
                
        
     
     
    
    