# ferran rojas
rut_cliente=""
coste_standard=5000
coste_premium=6500
coste_extra=1000
asientos_totales=0
ingreso_total=0
no_confirmadas=0
confirmadas=0
puntos_cinevid_cliente_totales=0
cine_vid_puntos_menores=99999999999999999999
rut_menores_puntos=""
while True or asientos_totales<70:
    monto=0
    asientos_cliente=0
    
    opcion=input("DESEA INGRESAR UNA RESERVA?:")
    while opcion not in ["s", "n"]:
        opcion=input("DESEA INGRESAR UNA RESERVA?:").lower()
    if opcion=="n":
        break
    
    rut_cliente=input("ingrese rut del cliente: ").lower()
    
    asientos_cliente=int(input("cuantos asientos desea reservar?: "))
    while asientos_cliente>5 or asientos_cliente<0:
        asientos_cliente=int(input("Valor invalido, debe ingresar un valor entre 1 y 5 y no mayor a 5\nCuantos asientos desea reservar?: "))
            
        
    asientos_standard=int(input("Cuantos asientos Standard desea reservar?: "))
    while asientos_standard>5 or asientos_standard<0 or asientos_standard>asientos_cliente:
        asientos_standard=int(input("Valor invalido, debe ingresar un valor entre 1 y 5 y no mayor a 5\nCuantos asientos Standard desea reservar?:  "))


    asientos_premium=int(input( "Cuantos asientos premium desea reservar?: "))
    while asientos_premium+asientos_standard>5 or asientos_premium>(asientos_cliente-asientos_standard):
        print(f"Valor invalido, debe ingresar un valor entre 1 y 5 y no mayor a {asientos_cliente-asientos_standard}")
        asientos_premium=int(input("Cuantos asientos premium desea reservar?: "))                     
        
        
    asientos_cliente=asientos_premium+asientos_standard
   
    monto=asientos_premium*coste_premium+asientos_standard*coste_standard
    
    
    proteccion_sanitaria=input("Desea agregar extra? (SI (S) - NO (N)):").lower()
    while proteccion_sanitaria not in ["s", "n"]:
        proteccion_sanitaria=input("Desea agregar extra? (SI (S) - NO (N)):")
    if proteccion_sanitaria=="s":
        mascarillas=int(input("Cuantas mascarillas faciales desea?: "))
        
    elif proteccion_sanitaria=="n":
        mascarillas=0
    monto+=mascarillas*coste_extra
    
    print(f"monto a cancelar es {monto}")
    
    confirmar=input("El cliente confirma la compra? (SI (S) - NO (N)): ").lower()
    while confirmar not in ["s", "n"]:
        confirmar=input("El cliente confirma la compra? (SI (S) - NO (N)): ").lower()
        
    puntos_cinevid_cliente=0
    
    if confirmar=="s":
        puntos_cinevid_cliente=monto/700
        confirmadas+=asientos_cliente
        if puntos_cinevid_cliente<cine_vid_puntos_menores:
            cine_vid_puntos_menores=puntos_cinevid_cliente
            rut_menores_puntos=rut_cliente
        
    elif confirmar=="n":
        multa=monto*0.15
        print(f"Dado que no efectuará la compra deberá cancelar una multa de: {multa} $")
        asientos_standard=0
        asientos_premium=0
        no_confirmadas+=asientos_cliente
        monto=0
        
        
    ingreso_total+=monto
     
    puntos_cinevid_cliente_totales+=puntos_cinevid_cliente
    
    asientos_totales+=asientos_premium+asientos_standard
    
    
        
        
    

porcentaje_ocupacion=(asientos_totales/70)*100
porcentaje_confirmadas=confirmadas/(confirmadas+no_confirmadas)*100
print(f"1. La cantidad de reservas confirmadas son {asientos_totales} \nEl porcentaje de reservas confirmadas es {porcentaje_confirmadas} %")
print(f"El ingreso total recibido por el cine es $ {ingreso_total}")
print(f" La cantidad total de puntos asignados es {puntos_cinevid_cliente_totales} ")
print(f"4. El rut de la persona que acumulo menor cantidad de puntos es {rut_menores_puntos} con {cine_vid_puntos_menores} puntos")
print(f" El porcentaje de utilización de la sala de cine es {porcentaje_ocupacion} %")





