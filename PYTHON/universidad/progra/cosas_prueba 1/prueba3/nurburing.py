arch=open("nurburgring_original.txt","r",encoding="utf-8")
linea=arch.readline().strip().lower()
distancia=20.6

modelo_mas_rapido=""
velocidad_mayor=0

empresa_auto_veloz=""
tiempo_de_auto_veloz=0

tiempo_auto_veloz=0
modelo_mas_lento_2018=""
segundos_menor_2018=0
empresa_2018_lento=""


modelos_totales=0
sumatoria_de_segundos=0

segundo_modelo_nuestro=440
velocidad_nuestro=(20.6*1000)/segundo_modelo_nuestro
contador_autos_mayores_2010=0
contador2_autos_mayores_2010=0
while linea!="":
    # datos_empresa
    velocidad_menor_2018=0
    partes=linea.split(",")
    empresa=partes[0]
    cantidad_modelos=int(partes[1])
    año_fundacion=int(partes[2])
    pais=partes[3]
        
    velocidad_mayor_empresa=0
    nombre_modelo_velocidad_mayor_empresa=""
    año_del_modelo_mayor=0
    segundos_auto_mayor_empresa=0
    
    modelos_totales+=cantidad_modelos
    for i in range(cantidad_modelos):
        # datos vehiculo
        linea=arch.readline().strip().lower()
        partes2=linea.split(";")
        nombre_modelo=partes2[0]
        minutos=float(partes2[1])
        segundos=float(partes2[2])
        año=int(partes2[3])
        segundos_totales=(minutos*60)+segundos
        velocidad=(20.6*1000)/segundos_totales
        if año>=2010:
            contador_autos_mayores_2010+=1
            if segundos_totales<440:
                contador2_autos_mayores_2010+=1
                
        
        sumatoria_de_segundos+=segundos_totales
        if velocidad>velocidad_mayor_empresa:
            velocidad_mayor_empresa=velocidad
            nombre_modelo_velocidad_mayor_empresa=nombre_modelo
            
            año_del_modelo_mayor_empresa=año
            segundos_auto_mayor_empresa=segundos_totales
            
       
            
            
        velocidad_menor_2018=velocidad_mayor
        if velocidad_menor_2018>velocidad and año==2018:
            modelo_mas_lento_2018=nombre_modelo
            velocidad_menor_2018=velocidad
            segundos_menor_2018=segundos_totales
            empresa_2018_lento=empresa
        
            
            
    
    if velocidad_mayor_empresa>velocidad_mayor:
        velocidad_mayor=velocidad_mayor_empresa
        modelo_mas_rapido=nombre_modelo_velocidad_mayor_empresa
        empresa_auto_veloz=empresa
        tiempo_auto_veloz=segundos_auto_mayor_empresa
        
   
    
        
            
        
    print(f"--{empresa} ({pais}) con {nombre_modelo_velocidad_mayor_empresa} con tiempo {segundos_auto_mayor_empresa} segundos en {año_del_modelo_mayor_empresa}")   
    linea=arch.readline().strip().lower()
    
porcentaje=(contador2_autos_mayores_2010/contador_autos_mayores_2010)*100
tiempo_promedio=sumatoria_de_segundos/modelos_totales
velocidad_promedio=distancia/(tiempo_promedio/3600)
print(f"2) El más rápido es {modelo_mas_rapido} de {empresa_auto_veloz} con un tiempo de {tiempo_auto_veloz} segundos")
print(f"3) El más lento del 2018 es {modelo_mas_lento_2018} de {empresa_2018_lento} con un tiempo de {segundos_menor_2018} segundos")
print(f"4) La velocidad promedio corresponde a {velocidad_promedio} km/h considerando un tiempo promedio de {tiempo_promedio} ")
print(f"5) El porcentaje de autos con tiempos inferiores a 7 minutos 20 segundos desde 2010 es {porcentaje} %")
    