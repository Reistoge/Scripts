#  Segun el archivo vuelos, crea un programa que determine lo siguiente:
# 1. Cantidad total de vuelos realizados
# 2. Cantidad de vuelos realizados hacia la ciudad de Santiago
# 3. Promedio de pasajeros transportados en los vuelos cuyo origen fue 
# Antofagasta o Santiago 
# 4. ÂCual fue el nombre de la ciudad de destino del viaje con mÃ¡s pasajeros? 
# Considera que es una sola
# 5. ÂCual fue el nombre de la ciudad de origen con el viaje con menos 
# pasajeros? Considera que es una sola
# 6. Porcentaje de vuelos que transportaron menos de 100 personas con 
# respecto al total de vuelos


### cuales fueron las ciudades de destino y origen con mas pasajeros ###

arch=open("ejercicio2.txt", "r",encoding="utf-8")
linea=arch.readline().strip()
info=""
pasajeros_total=0
pasajeros_mayor=0
pasajeros_menor=100000
pasajeros_stgo=0
pasajeros_antofa=0
nombre_pasaje_destino_mayor=""
nombre_pasaje_origen_menor=""
pasajeros_menores_a_100=0
vuelos=0
vuelos_stgo=0

while linea!="":
    vuelos+=1
    pasaje=linea.split(",")
    origen=pasaje[0].lower()
    destino=pasaje[1].lower()
    pasajeros=pasaje[2].lower()
    pasajeros=int(pasajeros)
    pasajeros_total+=pasajeros
    if pasajeros>pasajeros_mayor:
        ####debes actualizar la variable pasajeros mayor.
        nombre_pasaje_destino_mayor=destino
        pasajeros_mayor=pasajeros
        ##del vuelo mayor estamos tomando el destino
        
    if pasajeros<pasajeros_menor:
        ##actualiuza la variable pasajeros menor
        pasajeros_menor=pasajeros
        nombre_pasaje_origen_menor=origen
        ##del vuelo menor estamos tomando su origen
        
    if pasajeros<100:
        pasajeros_menores_a_100+=pasajeros
    if origen=="santiago":
        pasajeros_stgo+=pasajeros
        vuelos_stgo+=1
    elif origen=="antofagasta":
        pasajeros_antofa+=pasajeros
    linea=arch.readline()
    
promedio=pasajeros_stgo+pasajeros_antofa/2
porcentaje=(pasajeros_menores_a_100/pasajeros_total)*100
print("Total de vuelos realizados:", vuelos)
print("Vuelos realizados a Stgo:",vuelos_stgo)
print("Promedio de pasajeros transportados en los vuelos cuyo origen fue Antofagasta o Santiago", promedio)
print("Nombre de la ciudad de destino del viaje con m‡s pasajeros", nombre_pasaje_destino_mayor)
print("Nombre de la ciudad de origen con el viaje con menos pasajeros", nombre_pasaje_origen_menor)
print(f"Porcentaje de vuelos que transportaron menos de 100 personas con respecto al total de vuelos: {porcentaje:.3f}")
    
    
 
 
    
    

 