# El hotel cuenta con 10 habitaciones Standard 
# con un precio por noche de 120 dólares
# (USD) y 10 habitaciones Premium con un 
# valor de 250 dólares.
standard=120
premium=250
clientes=int(input("Cantidad de clientes a confirmar: "))
if clientes==0:
    print("Hoy no se han realizado llamados")
else:
    while clientes>20:
        clientes=int(input("Ingrese opción válida <20: "))
        
    clientes_confirmados=0
    cliente_que_mas_reservo=""
    dias_mas_reservados=0
    ingreso_confirmado=0
    ingreso_por_no_confirmar_total=0
    ingreso_dias_extra=0
    n_s=10
    n_p=10
    for i in range(0,clientes,1):
        precio_cliente=0.0
        nombre_del_cliente=input("Nombre del cliente: ").strip()
        dias_reservados=int(input("Días reservados por el cliente: "))
        
        tipo_tarifa=input("Tarifa (S/P): ").lower().strip()
        while tipo_tarifa not in ["s","p"]:
            tipo_tarifa=input("Ingrese opción válida (S/P): ").lower().strip()
        if tipo_tarifa=="s":
            precio_cliente=120*dias_reservados
             
        elif tipo_tarifa=="p":
            precio_cliente=250*dias_reservados
             
        confirmacion=input("Confirmación (S/N):").lower().strip()
        while confirmacion not in ["s","n"]:
            confirmacion=input("Ingrese opción válida (S/N): ").lower().strip()
        if confirmacion=="s":
            clientes_confirmados+=1
            dias_extra=int(input("Desea agregar más días a la reserva (ingrese 0 si no agrega): "))
            if dias_extra!=0 and tipo_tarifa=="s":
                dias_reservados+=dias_extra
                ingreso_dias_extra+=dias_extra*120
                precio_cliente=(dias_reservados)*120
                print(f"Reserva confirmada, total: USD {precio_cliente}")
                ingreso_confirmado+=precio_cliente
                
            elif dias_extra!=0 and tipo_tarifa=="p":
                
                dias_reservados+=dias_extra
                ingreso_dias_extra+=dias_extra*250
                precio_cliente=(dias_reservados)*250
                print(f"Reserva confirmada, total: USD {precio_cliente}")
                ingreso_confirmado+=precio_cliente
                
            elif dias_extra==0:
                # se mantiene
                precio_cliente=precio_cliente
                print(f"Reserva confirmada, total: USD {precio_cliente}")
                ingreso_confirmado+=precio_cliente
                
        
        if dias_reservados>dias_mas_reservados:
            dias_mas_reservados=dias_reservados
            cliente_que_mas_reservo=nombre_del_cliente
        
        elif confirmacion=="n":
            if tipo_tarifa=="s":
                n_s-=1
            elif tipo_tarifa=="p":
                n_p-=1
            ingreso_por_no_confirmar_total+=precio_cliente*0.25
            precio_cliente=0.75*precio_cliente
            print(f"Reserva cancelada, devolución: USD {precio_cliente}")

print(f"Hoy se ha confirmado a {clientes_confirmados} cliente(s) ({(clientes_confirmados/clientes)*100})%")
print(f"El cliente confirmado que más días reservó fue: {cliente_que_mas_reservo}")
print(f"El ingreso confirmado de hoy es: CLP {(ingreso_confirmado)*680}")
print(f"El ingreso por días extra agregados es: CLP {(ingreso_dias_extra)*680}")
# print(f"El posible ingreso por habitaciones libres es: CLP {(ingreso_por_no_confirmar_total)*680}")??? no se lo que hay que calcular sinceramente 
print(f"Habitaciones reservadas: {n_s} Standard {n_p} Premium")

        
   