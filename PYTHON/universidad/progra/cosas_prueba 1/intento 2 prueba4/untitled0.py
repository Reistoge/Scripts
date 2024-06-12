# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:12:22 2023

@author: Ferran Rojas
"""

arch1=open("config.txt","r",encoding="utf-8")
linea=(arch1.readline().strip().lower())
n_archivos=int(linea)
arch1.close()
def obtener_precio_por_metro(material_solicitado):
    
    arch1=open("config.txt","r",encoding="utf-8")
    arch1.readline()
    linea=(arch1.readline().strip().lower())
    while linea!="":
        partes=linea.split(",")
        material=partes[0]
        precio_carrete=float(partes[1])
        precio_metro=precio_carrete/330
        if material_solicitado==material:
            return precio_metro
        linea=(arch1.readline().strip().lower())

def formatear_minutos(minutos):
    dias=minutos//1440
    dias_resto=minutos%1440
    horas=dias_resto//60
    horas_restantes=dias_resto%60
    minutos=horas_restantes%60
    if dias!=0:
        x=(f"{dias} dias, {horas} horas, {minutos} minutos ")
    else:
        x=(f"{horas} horas, {minutos} minutos ")
        
    return x

    
formatear_minutos(59)
precio_total=0
piezas_calidad_alta=0
piezas_calidad_normal=0
piezas_totales=0
piezas=[]
contador=0
print(f"1) TIEMPOS")
for i in range(n_archivos):
    minutos_totales_pedido=0
    minutos_mayor=0
    minutos_menor=999999999999999
    id_pedido_menor_rapido=""
    id_pedido_mayor_lento=""
    
    nombre_archivo="P"+str(i+1)+".txt"
    
    print(f"\n***** Periodo {i+1} ******")
    arch=open(nombre_archivo)
    linea=arch.readline().strip().lower()
    while linea!="":
        metros=0
        piezas_totales+=1
        partes=linea.split("*")
        id_producto=partes[0]
        metros=float(partes[1])
        calidad=partes[2]
        material=partes[3]
        
        if material not in piezas:
            piezas.append(material)
            piezas.append(metros)
            
        elif material in piezas:
            for i in range(len(piezas)):
                if material==piezas[i]:
                    piezas[i+1]+=metros
    
       
        if material=="wood pla":
            contador+=metros
        
        if calidad=="alta":
            minutos_pedido=metros*46
            piezas_calidad_alta+=1
            
        elif calidad=="normal":
            minutos_pedido=metros*30
            piezas_calidad_normal+=1
            
        minutos_totales_pedido+=minutos_pedido
            
        if minutos_pedido>minutos_mayor:
            minutos_mayor=minutos_pedido
            id_pedido_mayor_lento=id_producto
        
        elif minutos_pedido<minutos_menor:
            minutos_menor=minutos_pedido
            id_pedido_menor_rapido=id_producto
            
        
        
        precio_pedido=obtener_precio_por_metro(material)*metros       
        precio_total+=precio_pedido
        linea=arch.readline().strip().lower()
        
    
    print(formatear_minutos(minutos_totales_pedido))
    print(f"más rapida {id_pedido_menor_rapido}\n{formatear_minutos(minutos_menor)}")
    print(f"más extensa {id_pedido_mayor_lento}\n{formatear_minutos(minutos_mayor)}")
porcentaje_altas=(piezas_calidad_alta/piezas_totales)*100
porcentaje_normales=(piezas_calidad_normal/piezas_totales)*100

print(f"se imprimiran {piezas_totales} piezas ")
print(f"con un {porcentaje_altas}% de piezas altas")
print(f"con un {porcentaje_normales}% de piezas normales")

for i in range(0, len(piezas),2):
    print(piezas[i],piezas[i+1])

print(f"{precio_total}")
  
        
        

        

    