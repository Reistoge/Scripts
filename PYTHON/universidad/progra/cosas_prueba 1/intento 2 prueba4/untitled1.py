# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:55:23 2023

@author: Ferran Rojas
"""

def opcion_1():
    contador_patente_solicitada=0
    patente_solicitada=input("ingrese la patente: ").lower()
    arch=open("estacionados.txt","r",encoding="utf-8")
    linea=arch.readline().strip().lower()
    while linea!="":
        patente=linea.split(",")[0]
        terminacion_patente=patente.split("-")[-1]
        
        if patente_solicitada=="-":
            contador_patente_solicitada+=1
            
        elif terminacion_patente==patente_solicitada:
            contador_patente_solicitada+=1
        
            
        linea=arch.readline().strip().lower()
    
    print( contador_patente_solicitada)


    
        

def opcion_2():
 
    arch=open("estacionados.txt","r",encoding="utf-8")
    linea=arch.readline().strip().lower()
    pasaje_libre=0
    pasajes=0
    while linea!="":
        pasajes+=1
        partes=linea.strip().split(",")
        horas_llegada=int(partes[1])
        minutos_llegada=int(partes[2])
        horas_salida=int(partes[3])
        minutos_salida=int(partes[4])
        estadia=((horas_salida*60)+minutos_salida)-((horas_llegada*60)+minutos_llegada)
        if estadia<30:
            pasaje_libre+=1
        linea=arch.readline().strip().lower()
    porcentaje=pasaje_libre/pasajes
    print(f" Un {porcentaje*100}% de los vehículos tuvo pase libre")
def opcion_3():
    costo_por_minuto=float(input("Costo por minuto: "))
    Min_libres=float(input("Minutos libres: "))
    patente_menor=""
    minutos_menor=999999999999999
    precio_estadia_menor=0
    arch=open("estacionados.txt","r",encoding="utf-8")
    linea=arch.readline().strip().lower()
    while linea!="":
        partes=linea.strip().split(",")
        patente=partes[0]
        horas_llegada=int(partes[1])
        minutos_llegada=int(partes[2])
        horas_salida=int(partes[3])
        minutos_salida=int(partes[4])
        min_estadia=((horas_salida*60)+minutos_salida)-((horas_llegada*60)+minutos_llegada)
        if min_estadia<Min_libres:
            precio_estadia=0
            
        elif min_estadia>Min_libres:
            precio_estadia=min_estadia*costo_por_minuto
            
        if min_estadia<minutos_menor and precio_estadia!=0:
            minutos_menor=min_estadia
            patente_menor=patente
            precio_estadia_menor=minutos_menor*costo_por_minuto
        
        linea=arch.readline().strip().lower()
    print(f" 3) El vehículo que menos pagó fue {patente_menor} pagando un total de {precio_estadia_menor}")
        
    
    
# def opcion_3():
    
        
while True:
    opcion=input("Ingrese opción (1, 2 o 3, -1 para terminar): ")
    while opcion not in ["1","2","3","-1"]:
        opcion=input("Error (1, 2 o 3, -1 para terminar): ")
    if opcion=="1":
        opcion_1()
    elif opcion=="2":
        opcion_2()
    elif opcion=="3":
        opcion_3()
    if opcion=="-1":
        print("saliendo")
        break

    