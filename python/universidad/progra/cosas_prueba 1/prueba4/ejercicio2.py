
def obtener_patente(patente_solicitada):
    arch1=open("estacionados.txt","r",encoding="utf-8")
    linea=arch1.readline().strip().lower()
    suma_patente=0
    while linea!="":
        partes=linea.split(",")
        patente=partes[0]
        terminacion_patente=patente.split("-")[-1]
        if patente_solicitada=="-":
            suma_patente+=1
        if terminacion_patente==patente_solicitada and patente_solicitada!="-":
            suma_patente+=1
        
        linea=arch1.readline().strip().lower()
            
    arch1.close()
    return suma_patente
def Porcentaje_de_vehículos_que_tuvo_pase_libre():
    arch1=open("estacionados.txt","r",encoding="utf-8")
    linea=arch1.readline().strip().lower()
    pase_libre=0
    total=0
    while linea!="":
        total+=1
        partes=linea.split(",")
        hora_llegada=int(partes[1])
        minutos_llegada=int(partes[2])
        hora_salida=int(partes[3])
        minutos_salida=int(partes[4])
        if (hora_salida-hora_llegada)==0 and (minutos_salida-minutos_llegada)<30:
            pase_libre+=1
        linea=arch1.readline().strip().lower()
    porcentaje=round((pase_libre/total)*100)
    print(f"Un {porcentaje}% de los vehículos tuvo pase libre")
    
def vehículo_pagó_menos_por_su_estadía_y_la_cantidad_pagada():
    costo_minuto=int(input("Costo por minuto: "))
    minutos_libres=int(input("Minutos libres: "))
    arch1=open("estacionados.txt","r",encoding="utf-8")
    linea=arch1.readline().strip().lower()
    precio_menor=100000000000000.0
    tiempo_menor=0
    patente_menor=""
    while linea!="":
        partes=linea.split(",")
        patente=partes[0]
        hora_llegada=int(partes[1])
        minutos_llegada=int(partes[2])
        hora_salida=int(partes[3])
        minutos_salida=int(partes[4])
        tiempo_minutos=float(((hora_salida*60)+(minutos_salida))-((hora_llegada*60)+(minutos_llegada)))
        precio=tiempo_minutos*costo_minuto
        
        if precio<precio_menor and tiempo_minutos>=minutos_libres:
            precio_menor=precio
            patente_menor=patente
            tiempo_menor=tiempo_minutos
        linea=arch1.readline().strip().lower()
    print(f" El vehículo que menos pagó fue {patente_menor} pagando un total de {precio_menor}")
        
# menu

while True:
    opcion=input("Ingrese opción (1, 2 o 3, -1 para terminar): ")
    while opcion not in ["1","2","3","-1"]:
        opcion=input("Error (1, 2 o 3, -1 para terminar): ")
    if opcion=="-1":
        break
    elif opcion=="1":
        suma=obtener_patente(input("Ingrese terminación de patente: ").lower())
        print(f"1) Cantidad de autos estacionados: {suma}")
    elif opcion=="2":
        Porcentaje_de_vehículos_que_tuvo_pase_libre()
    elif opcion=="3":
        vehículo_pagó_menos_por_su_estadía_y_la_cantidad_pagada()
        
    
  
    
 



